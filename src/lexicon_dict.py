from src.lexicon import Lexicon
from src.word_tree import WordTree, Word

# TODO: Write docstrings

class LexiconDict(Lexicon):
    def __init__(self):
        super().__init__()
        self.dictionary: dict[str, Word] = {}

    def insert_element(self, data):
        pass
        # self.dictionary ...

    def populate_lists(self):
        pass

    def reset(self):
        """Resets the LexiconDict."""
        self.dictionary.clear()
        super().reset()

