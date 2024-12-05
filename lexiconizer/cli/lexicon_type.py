from typing import Callable

class LexiconType:
    def __init__(
        self,
        lexicon_type: type,
        flags: list[str],
        help: str,
        sorting_method: Callable=None
    ):
        self.lexicon_type: type = lexicon_type
        self.flags: list[str] = flags
        self.help: str = help
        self.sorting_method: Callable = sorting_method
        self.name: str = self.get_name(flags)
        self.filename: str = None

    @staticmethod
    def get_name(flags: list[str]):
        name_flag = LexiconType.get_name_flag(flags)
        name_split = name_flag.split('-')
        name = '_'.join(_ for _ in name_split if _ != '')
        return name

    @staticmethod
    def get_name_flag(flags: list[str]):
        for i in reversed(range(2)):
            try:
                return flags[i]
            except IndexError:
                continue
        raise ValueError('Error: Flags is empty.')
