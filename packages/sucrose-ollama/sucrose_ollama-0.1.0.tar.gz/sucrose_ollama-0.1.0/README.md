# Sucrose

Inspired by `fructose` https://github.com/bananaml/fructose, but uses the ollama python client. Supports `pydantic` models.

```
pip install sucrose
```

```python
from sucrose import Sucrose
ai = Sucrose()

@ai
def describe(animals: list[str]) -> str:
  """
  Given a list of animals, use one word that'd describe them all.
  """
  ...

description = describe(["dog", "cat", "parrot", "goldfish"])
print(description) # -> "pets" type: str
```
