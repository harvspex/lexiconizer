from src.lexicon import Lexicon
from src.word import Word
from utils.neighbours_utils import add_to_inner

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
        self.sorted_list = [_ for _ in self.dictionary.values()]

    def reset(self):
        """Resets the LexiconDict."""
        self.dictionary.clear()
        super().reset()
