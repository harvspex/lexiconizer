from lexicon.lexicon import Lexicon
from data_structures.word_tree import WordTree

# TODO: Rewrite docstrings

class LexiconAVL(Lexicon):
    """
    A class for managing a lexicon of words stored in an AVL Tree structure.

    The Lexicon supports reading words from files, finding neighboring 
    words, and saving results to an output file.

    Attributes:
        word_tree (WordTree): The AVL Tree storing words.
        sorted_list (list[Word]): A list of words in sorted order.
        one_char_words (list[Word]): A sorted list of one-letter words.
        nested_word_lists (list): A list of words nested by: word length, then char 1, then char 0.
    """
    def __init__(self):
        super().__init__()
        self.word_tree = WordTree()

    def insert_element(self, data: str):
        self.word_tree.insert_element(data)

    def populate_lists(self):
        self.word_tree.traverse_inorder(
            self.word_tree.root,
            self.sorted_list,
            self.one_char_words,
            self.nested_word_list
        )

    def reset(self):
        """Resets the LexiconAVL."""
        self.word_tree = WordTree()
        super().reset()
