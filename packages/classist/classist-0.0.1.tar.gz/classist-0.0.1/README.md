# Classist

Pretty classist signature inheritance with decorators.

## Features

This is just a basic proof of concept. Currently, only very basic runtime
signature inheritance is implemented. It may be possible to generate stubs to
support static type checking.

## Usage

```python
import classist
import inspect

class A:
    def __init__(self, a: int):
        self.a = a

@classist.decorate
class B:
    def __init__(self, t: int, *args):
        self.b = b
        super().__init__(*args)

print(inspect.signature(B.__init__))
```

## Installation

```bash
pip install classist
```
