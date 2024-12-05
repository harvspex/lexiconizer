from typing import Callable

class LexiconType:
    """
    Represents a type of lexicon with its associated CLI flags and properties.

    Attributes:
        lexicon_type (type): Class type of the lexicon to be generated.
        flags (list[str]): CLI flags associated with this lexicon type.
        help (str): The help text for the CLI flags.
        sorting_method (Callable): An optional sorting function for the
            lexicon.
        name (str): The name of the lexicon derived from its flags.
        filename (str): The output filename for the lexicon, assigned
            during runtime.
    """
    def __init__(
        self,
        lexicon_type: type,
        flags: list[str],
        help: str,
        sorting_method: Callable=None
    ):
        """
        Initializes a LexiconType instance.

        Args:
            lexicon_type (type): Class type of the lexicon to be
                generated.
            flags (list[str]): The CLI flags associated with this
                lexicon type.
            help (str): The help text for the CLI flags.
            sorting_method (Callable, optional): An optional sorting
                function for the lexicon.
        """
        self.lexicon_type: type = lexicon_type
        self.flags: list[str] = flags
        self.help: str = help
        self.sorting_method: Callable = sorting_method
        self.name: str = self.get_name(flags)
        self.filename: str = None

    @staticmethod
    def get_name(flags: list[str]):
        """
        Derives the name of the lexicon from its CLI flags.

        Args:
            flags (list[str]): The CLI flags associated with the lexicon

        Returns:
            str: The derived name of the lexicon.
        """
        name_flag = LexiconType.get_name_flag(flags)
        name_split = name_flag.split('-')
        name = '_'.join(_ for _ in name_split if _ != '')
        return name

    @staticmethod
    def get_name_flag(flags: list[str]):
        """
        Retrieves the preferred flag to use as the lexicon name.

        Args:
            flags (list[str]): The CLI flags associated with the lexicon

        Returns:
            str: The preferred flag to use as the lexicon name.

        Raises:
            ValueError: If the flags list is empty.
        """
        for i in reversed(range(2)):
            try:
                return flags[i]
            except IndexError:
                continue
        raise ValueError('Error: Flags is empty.')
