from lexiconizer.lexicons.lexicon import Lexicon
from lexiconizer.data_structures.word_tree import WordTree

# TODO: Rewrite docstrings

class LexiconAVL(Lexicon):
    """
    A lexicon implemented using an AVL Tree for word storage and management.

    Attributes:
        word_tree (WordTree): An AVL Tree for storing and managing words.
    """
    def __init__(self):
        """
        Initializes an AVL Tree-based lexicon.
        """
        super().__init__()
        self.word_tree = WordTree()

    def insert_element(self, data: str):
        """
        Inserts a word into the AVL Tree.

        Args:
            data (str): The word to insert.
        """
        self.word_tree.insert_element(data)

    def populate_lists(self):
        """
        Populates internal lists by traversing the AVL Tree in order.
        """
        self.word_tree.traverse_inorder(
            self.word_tree.root,
            self.sorted_list,
            self.one_char_words,
            self.nested_word_list
        )

    def reset(self):
        """
        Resets the AVL Tree and other internal lists.
        """
        self.word_tree = WordTree()
        super().reset()
