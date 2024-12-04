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

    # TODO: Improve
    @staticmethod
    def get_name(flags: list[str]):
        name_flag = flags[1]
        name_split = name_flag.split('-')
        name = '_'.join(_ for _ in name_split if _ != '')
        return name
