from typing import Callable
from lexiconizer.lexicons.lexicon import Lexicon
from lexiconizer.shared.word import Word
from lexiconizer.utils.neighbours_utils import add_word_to_nested_list

# TODO: Write docstrings

class LexiconDict(Lexicon):
    def __init__(self, sorting_method: Callable=sorted):
        super().__init__()
        self.dictionary: dict[str, Word] = {}
        self.sorting_method: Callable = sorting_method

    def insert_element(self, data: str):
        try:
            self.dictionary[data].frequency += 1
        except:
            self.dictionary[data] = Word(data)

    def sort_dictionary(self):
        keys: list[str] = list(self.dictionary.keys())
        keys = self.sorting_method(keys)
        self.sorted_list = [self.dictionary[word] for word in keys]

    def populate_lists(self):
        self.sort_dictionary()

        for word in self.sorted_list:
            add_word_to_nested_list(word, self.nested_word_list, self.one_char_words)

    def reset(self):
        """Resets the LexiconDict."""
        self.dictionary.clear()
        super().reset()
