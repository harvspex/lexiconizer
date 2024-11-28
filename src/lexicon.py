from src.word_tree import WordTree, Word
import utils.one_char_utils as one_char_utils
import utils.same_char_0_utils as same_char_0_utils
import utils.same_char_1_utils as same_char_1_utils

# NOTE: staticmethods may be slower. Do testing.
# TODO: init with filename, and run build_lexicon on init?
# TODO: Could add option to time build_lexicon subtasks individually
# TODO: Finish adding type hints

class Lexicon:
    """
    A class for managing a lexicon of words stored in an AVL Tree structure.
    The Lexicon supports reading words from files, finding neighboring words,
    and saving results to an output file.

    Attributes:
        word_tree (WordTree): The AVL Tree storing words.
        sorted_list (list[Word]): A list of words in sorted order.
        one_char_words (list[Word]): A sorted list of one-letter words.
        nested_word_lists (list): A list of words nested by: word length, then char 1, then char 0.
    """

    def __init__(self):
        self.word_tree = WordTree()
        self.sorted_list: list[Word] = []
        self.one_char_words: list[Word] = [] # Could potentially be list[str]
        self.nested_word_lists: list = []

    def read_data(self, filename):
        """
        Reads text data from a file and inserts it into the Lexicon's AVL Tree.

        Args:
            filename (str): The path to the input file containing words.

        Raises:
            IOError: If the file cannot be read.
        """
        # TODO: actually raise the error
        with open(filename, 'r') as infile:
            for line in infile:
                tokens = line.lower().strip().split()

                for token in tokens:
                    data = ''.join(c for c in token if c.isalpha())

                    if data:
                        self.word_tree.insert_element(data)

    def write_to_file(self, filename):
        """
        Writes the sorted list of words to a file.

        Args:
            filename (str): The path to the output file where data will be written.

        Raises:
            IOError: If the file cannot be written.
        """
        # TODO: Actually raise the error
        with open(filename, 'w') as outfile:
            for i in self.sorted_list:
                outfile.write(str(i))

    def add_all_neighbours(self):
        """
        Executes all neighbor-finding methods, including:
            `one_char_utils.add_neighbours`
            `same_char_0_utils.add_neighbours`
            `same_char_1_utils.add_neighbours`
        """
        one_char_utils.add_neighbours(self.one_char_words)
        same_char_0_utils.add_neighbours(self.nested_word_lists)
        same_char_1_utils.add_neighbours(self.nested_word_lists)

    def reset(self):
        """Resets the lexicon."""
        self.word_tree = WordTree()
        self.sorted_list.clear()
        self.one_char_words.clear()
        self.nested_word_lists.clear()

    def build_lexicon(self, input_filename, output_filename='out.txt', reset=True):
        """
        Builds the Lexicon by processing an input file, identifying neighbors, and saving results.

        Args:
            input_filename (str): The path to the input file containing words.
            output_filename (str): The path to the output file (default: 'out.txt').
            reset (bool): Whether to reset the Lexicon before building (default: True).
        """

        if reset: self.reset()

        # Generate AVL Tree
        print('Inserting data into AVL Tree...')
        self.read_data(input_filename)

        # Populate lists
        print('Populating lists...')
        self.word_tree.traverse_inorder(self.word_tree.root, self.sorted_list, self.one_char_words, self.nested_word_lists)

        # Add neighbours
        print('Adding neighbours...')
        self.add_all_neighbours()

        # Write to file
        print('Writing to file...')
        self.write_to_file(output_filename)

        print('Finished!\n')
