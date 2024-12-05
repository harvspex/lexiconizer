from typing import Callable

# TODO: Docstring
class FuncClass:
    """
    A class for encapsulating functions along with their descriptions and arguments.

    This class is used to manage functions and their metadata for structured 
    execution in a pipeline, such as building a lexicon.

    Attributes:
        name (Callable): The function to be executed.
        description (str): A description of what the function does. Printed in
            verbose mode.
        args (tuple): Positional arguments to pass to the function.
        kwargs (dict): Keyword arguments to pass to the function.
    """
    def __init__(self, name: Callable, description: str, *args, **kwargs):
        """
        Initializes a `FuncClass` instance with the function, description, 
        and arguments.

        Args:
            name (Callable): The function to be executed.
            description (str): A description of what the function does. Printed in
                verbose mode.
            *args: Positional arguments for the function.
            **kwargs: Keyword arguments for the function.
        """
        self.name = name
        self.description = description
        self.args = args
        self.kwargs = kwargs
