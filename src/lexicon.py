from abc import ABC, abstractmethod
from src.word import Word
from src.func_class import FuncClass
from utils.test_utils import time_method
import utils.one_char_utils as one_char_utils
import utils.same_char_0_utils as same_char_0_utils
import utils.same_char_1_utils as same_char_1_utils

# TODO: Handle IOError if files cannot be read
# TODO: Write docstrings

class Lexicon(ABC):
    def __init__(self):
        self.sorted_list: list[Word] = []
        self.one_char_words: list[Word] = []
        self.nested_word_list: list = []

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

                    if data: self.insert_element(data)

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
        same_char_0_utils.add_neighbours(self.nested_word_list)
        same_char_1_utils.add_neighbours(self.nested_word_list)

    def reset(self):
        """Resets the lexicon."""
        self.sorted_list.clear()
        self.one_char_words.clear()
        self.nested_word_list.clear()

    def build_lexicon(
        self,
        input_filename: str,
        output_filename: str,
        reset: bool=True,
        time: bool=False,
        n_repeats: int=1,
        verbose: bool=False
    ):
        # TODO: REword
        """
        Builds the Lexicon. Processes input, adds neighbors, and saves results.

        Args:
            input_filename (str): The path to the input file containing words.
            output_filename (str): The path to the output file.
            reset (bool): Whether to reset the Lexicon before building
                (default: True).
        """

        # TODO: This works but isn't great
        # Try timing the whole "build lexicon" elsewhere, e.g. in lexiconizer.py
        args = input_filename, output_filename, reset, time, verbose

        if time:
            time_method(
                self.build_lexicon_helper,
                *args,
                n_repeats=n_repeats,
                verbose=verbose,
            )

        else:
            self.build_lexicon_helper(*args)

    def build_lexicon_helper(
        self,
        input_filename: str,
        output_filename: str,
        reset: bool=True,
        time: bool=False,
        verbose: bool=False
    ):
        funcs = [
            FuncClass(self.read_data, 'Reading and inserting data...', input_filename),
            FuncClass(self.populate_lists, 'Populating lists...'),
            FuncClass(self.add_all_neighbours, 'Adding neighbours...'),
            FuncClass(self.write_to_file, 'Writing to file...', output_filename)
        ]

        print(f'time={time} verbose={verbose}')

        if reset: self.reset()

        for f in funcs:
            if time or verbose:
                print(f.description)

            if time:
                time_method(f.name, *f.args, **f.kwargs)
            else:
                f.name(*f.args, **f.kwargs)

        if time != verbose:
            print('Finished!')
