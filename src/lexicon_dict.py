from src.lexicon import Lexicon
from src.word import Word
from utils.neighbours_utils import add_word_to_nested_list

# TODO: Write docstrings

class LexiconDict(Lexicon):
    def __init__(self):
        super().__init__()
        self.dictionary: dict[str, Word] = {}

    def insert_element(self, data: str):
        try:
            self.dictionary[data].frequency += 1
        except:
            self.dictionary[data] = Word(data)

    def populate_lists(self):
        self.dictionary = dict(sorted(self.dictionary.items()))
        self.sorted_list = list(self.dictionary.values())

        for word in self.sorted_list:
            add_word_to_nested_list(word, self.nested_word_list, self.one_char_words)

    def reset(self):
        """Resets the LexiconDict."""
        self.dictionary.clear()
        super().reset()
