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
        self.name: str = self.get_name(flags)
        self.filename = self.name
        self.sorting_method = sorting_method

    # TODO: Improve
    @staticmethod
    def get_name(flags: list[str]):
        name_flag = flags[1]
        name_split = name_flag.split('-')
        name = '_'.join(_ for _ in name_split if _ != '')
        return name

    def __str__(self):
        return f'{self.lexicon_type} {self.flags} {self.help} {self.name} {self.filename} {self.sorting_method}'