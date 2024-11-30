from abc import ABC, abstractmethod
from src.word_tree import Word
import utils.one_char_utils as one_char_utils
import utils.same_char_0_utils as same_char_0_utils
import utils.same_char_1_utils as same_char_1_utils

# TODO: init with filename, and run build_lexicon on init?
# TODO: Add option to time build_lexicon subtasks individually
# TODO: Handle IOError if files cannot be read
# TODO: Write docstrings

class Lexicon(ABC):
    def __init__(self):
        self.one_char_words: list[Word] = []
        self.nested_word_lists: list = []

    # @abstractmethod
    # def read_data(self, filename: str): pass

    @abstractmethod
    def insert_element(self, data: str): pass

    @abstractmethod
    def populate_lists(self): pass

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
                        self.insert_element(data)

    def write_to_file(self, filename: str):
        """
        Writes the sorted list of words to a file.

        Args:
            filename (str): The path to the output file where data will be written.

        Raises:
            IOError: If the file cannot be written.
        """
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
        self.one_char_words.clear()
        self.nested_word_lists.clear()

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

        print('Reading and inserting data...')
        self.read_data(input_filename)

        print('Populating lists...')
        self.populate_lists()

        print('Adding neighbours...')
        self.add_all_neighbours()

        print('Writing to file...')
        self.write_to_file(output_filename)

        print('Finished!\n')
