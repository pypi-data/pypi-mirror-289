import json
import functools

import ollama
from pydantic import BaseModel, create_model
from inspect import signature
from typing_utils import issubtype
from jsf import JSF

__all__ = ["Sucrose"]


class Sucrose:
    def __init__(self, model_name: str = "llama3"):
        self.model_name = model_name

        self.registered_fns = {}

    def __call__(self, func=None, use_schema=True, use_examples=True):
        if func is None:
            return lambda func: self.__call__(
                func, use_schema=use_schema, use_examples=use_examples
            )

        assert func.__doc__, f"Agent {func.__name__} does not have a docstring"
        self.registered_fns[func.__name__] = func
        fn_signature = signature(func)
        return_annotation = fn_signature.return_annotation
        using_tmp_model = False
        if not issubtype(return_annotation, BaseModel):
            base_model = create_model(
                f"TmpResponse_{func.__name__}", response=(return_annotation, ...)
            )
            using_tmp_model = True
        else:
            base_model = return_annotation

        schema = base_model.model_json_schema()
        faker = JSF(schema)
        examples = [
            faker.generate(),
            faker.generate(),
            faker.generate(),
        ]

        @functools.wraps(func)
        def inner(*args, **kwargs):
            inputs = fn_signature.bind(*args, **kwargs)
            formatted_inputs = []

            for k, v in inputs.arguments.items():
                if isinstance(v, BaseModel):
                    formatted_inputs.append(f"{k}={v.model_dump()}")
                else:
                    tmp_model = create_model("TmpModel", param=(type(v), ...))
                    tmp_model_instance = tmp_model(param=v)
                    v = tmp_model_instance.model_dump()["param"]
                    formatted_inputs.append(f"{k}={v}")

            inputs_str = "\n".join(formatted_inputs)
            # print('--', inputs_str)
            if use_schema:
                system_schemas_str = f"""Your response should be in JSON format following this schema:
```
{schema}
```"""
            else:
                system_schemas_str = ""
            if use_examples:
                system_examples_str = f"""
Here are some examples:
Example 1:
```{json.dumps(examples[0], indent=2)}```
Example 2:
```{json.dumps(examples[1], indent=2)}```
Example 3:
```{json.dumps(examples[2], indent=2)}```
Note these examples are fake and should just be used as examples of the schema, i.e.
don't return fake data like latin, you should return actual data that matches your functionality.
                """
            else:
                system_examples_str = ""

            messages = [
                {
                    "role": "system",
                    "content": f"""You're a system called `{func.__name__}` that provides the following functionality:
```
{func.__doc__}
```
{system_schemas_str}
{system_examples_str}""",
                },
                {
                    "role": "user",
                    "content": f"""Given the following input:
{inputs_str}
Provide the appropriate JSON response.""",
                },
            ]
            print("-messages", messages)
            response = ollama.chat(
                model=self.model_name, messages=messages, format="json"
            )
            content = response["message"]["content"]
            print("---content", content)
            print("--basemodel", base_model)
            parsed = base_model.model_validate_json(content)
            if using_tmp_model:
                return parsed.response
            else:
                return parsed

        return inner

    def get_inputs(self, name):
        func = self.registered_fns[name]
        sig = signature(func)
        inputs = {}
        for param in sig.parameters.values():
            inputs[param.name] = param.annotation
        return inputs
