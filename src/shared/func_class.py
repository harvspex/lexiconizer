from typing import Callable

# TODO: Docstring
class FuncClass:
    def __init__(self, name: Callable, description: str, *args, **kwargs):
        self.name = name
        self.description = description
        self.args = args
        self.kwargs = kwargs
