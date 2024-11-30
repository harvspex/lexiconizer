# TODO: Should be a subclass of Lexicon, using a word_tree

from src.lexicon import Lexicon
from src.word_tree import WordTree, Word

# NOTE: staticmethods may be slower. Do testing.
# TODO: init with filename, and run build_lexicon on init?
# TODO: Could add option to time build_lexicon subtasks individually
# TODO: Handle IOError if files cannot be read

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
        self.sorted_list: list[Word] = []

    def read_data(self, filename: str):
        """
        Reads text data from a file and inserts it into the Lexicon's AVL Tree.

        Args:
            filename (str): The path to the input file containing words.

        Raises:
            IOError: If the file cannot be read.
        """
        with open(filename, 'r') as infile:
            for line in infile:
                tokens = line.lower().strip().split()

                for token in tokens:
                    data = ''.join(c for c in token if c.isalpha())

                    if data:
                        self.word_tree.insert_element(data)

    def reset(self):
        """Resets the LexiconAVL."""
        self.word_tree = WordTree()
        self.sorted_list.clear()
        super().reset()

    def build_lexicon(self, input_filename: str, output_filename: str, reset: bool=True):
        """
        Builds the Lexicon. Processes input, adds neighbors, and saves results.

        Args:
            input_filename (str): The path to the input file containing words.
            output_filename (str): The path to the output file.
            reset (bool): Whether to reset the Lexicon before building
                (default: True).
        """

        if reset: self.reset()

        # Generate AVL Tree
        print('Inserting data into AVL Tree...')
        self.read_data(input_filename)

        # Populate lists
        print('Populating lists...')
        self.word_tree.traverse_inorder(
            self.word_tree.root,
            self.sorted_list,
            self.one_char_words,
            self.nested_word_lists
        )

        super().build_lexicon(input_filename, output_filename)