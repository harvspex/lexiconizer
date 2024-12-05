from abc import ABC, abstractmethod
from lexiconizer.shared.word import Word
from lexiconizer.shared.func_class import FuncClass
from lexiconizer.utils.test_utils import time_method
import lexiconizer.utils.one_char_utils as one_char_utils
import lexiconizer.utils.same_char_0_utils as same_char_0_utils
import lexiconizer.utils.same_char_1_utils as same_char_1_utils

class Lexicon(ABC):
    """
    Abstract base class for managing lexicons.

    This class defines the structure for lexicon management, including 
    reading and writing data, resetting the lexicon, and adding neighbors 
    based on specific criteria.

    Attributes:
        sorted_list (list[Word]): A list of words in sorted order.
        one_char_words (list[Word]): A list of words with only one character
        nested_word_list (list): A nested list of words based on custom
            criteria.
    """
    def __init__(self):
        """
        Initializes an empty lexicon with sorted lists and nested lists.
        """
        self.sorted_list: list[Word] = []
        self.one_char_words: list[Word] = []
        self.nested_word_list: list = []

    @abstractmethod
    def insert_element(self, data: str):
        """
        Abstract method for inserting an element into the lexicon.

        Args:
            data (str): The word to insert.
        """
        pass

    @abstractmethod
    def populate_lists(self):
        """
        Abstract method to populate internal lists after data insertion.
        """
        pass

    def read_data(self, filename: str):
        """
        Reads text data from a file and inserts into Lexicon.

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
        verbose: bool=False,
        time: bool=False,
        reset: bool=True
    ):
        """
        Builds the Lexicon. Processes input, adds neighbors, and saves results.

        Args:
            input_filename (str): The path to the input file containing words.
            output_filename (str): The path to the output file.
            verbose (bool): Whether to print the function's description before
                execution (default: False).
            time (bool): Whether to measure and print the execution time
                (default: False).
            reset (bool): Whether to reset the Lexicon before building
                (default: True).
        """
        funcs = self.get_build_lexicon_funcs(input_filename, output_filename)

        if reset: self.reset()

        for func in funcs:
            Lexicon.execute_func(func, verbose, time)

        if time or verbose:
            print('Finished!\n')

    def get_build_lexicon_funcs(self, input_filename: str, output_filename: str,) -> list[FuncClass]:
        """
        Creates a list of functions to execute for building the lexicon.

        Each function in the list is wrapped in a `FuncClass` instance, which 
        includes a reference to the function, a description, and its arguments.

        Args:
            input_filename (str): The path to the input file containing words.
            output_filename (str): The path to the output file where results are
                saved.

        Returns:
            list[FuncClass]: A list of functions required for building the lexicon.
        """
        funcs = [
            FuncClass(self.read_data, 'Reading and inserting data...', input_filename),
            FuncClass(self.populate_lists, 'Sorting lexicon...'),
            FuncClass(self.add_all_neighbours, 'Adding neighbours...'),
            FuncClass(self.write_to_file, 'Writing to file...', output_filename)
        ]
        return funcs

    @staticmethod
    def execute_func(func: FuncClass, verbose: bool, time: bool):
        """
        Executes a function wrapped in a `FuncClass` instance.

        Depending on the `verbose` and `time` flags, it prints a description 
        and/or measures the execution time.

        Args:
            func (FuncClass): The function to execute, encapsulated in a
                `FuncClass`.
            verbose (bool): Whether to print the function's description before
                execution.
            time (bool): Whether to measure and print the execution time.
        """
        if time or verbose:
            print(func.description)

        if time:
            time_method(func.name, *func.args, **func.kwargs)
        else:
            func.name(*func.args, **func.kwargs)
