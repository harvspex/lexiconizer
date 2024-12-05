from typing import Callable
from lexiconizer.lexicons.lexicon import Lexicon
from lexiconizer.shared.word import Word
from lexiconizer.utils.neighbours_utils import add_word_to_nested_list

class LexiconDict(Lexicon):
    """
    A dictionary-based implementation of the Lexicon.

    Attributes:
        dictionary (dict[str, Word]): A dictionary where keys are words and 
            values are Word objects.
        sorting_method (Callable): The method used for sorting the lexicon.
    """
    def __init__(self, sorting_method: Callable=sorted):
        """
        Initializes a dictionary-based lexicon with a sorting method.

        Args:
            sorting_method (Callable): The sorting function to use (default: `sorted`).
        """
        super().__init__()
        self.dictionary: dict[str, Word] = {}
        self.sorting_method: Callable = sorting_method

    def insert_element(self, data: str):
        """
        Inserts a word into the lexicon, updating its frequency if it already exists.

        Args:
            data (str): The word to insert.
        """
        try:
            self.dictionary[data].frequency += 1
        except:
            self.dictionary[data] = Word(data)

    def sort_dictionary(self):
        """
        Sorts the dictionary keys using the specified sorting method 
        and updates the sorted list.
        """
        keys: list[str] = list(self.dictionary.keys())
        keys = self.sorting_method(keys)
        self.sorted_list = [self.dictionary[word] for word in keys]

    def populate_lists(self):
        """
        Populates internal lists after sorting the dictionary.
        """
        self.sort_dictionary()

        for word in self.sorted_list:
            add_word_to_nested_list(word, self.nested_word_list, self.one_char_words)

    def reset(self):
        """
        Resets the LexiconDict, clearing the dictionary and other lists.
        """
        self.dictionary.clear()
        super().reset()
