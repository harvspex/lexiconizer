from lexiconizer.lexicons.lexicon_dict import LexiconDict
from lexiconizer.sorting.radix_sort import radix_sort

class LexiconRadix(LexiconDict):
    """
    A dictionary-based lexicon using radix sort for sorting.

    Attributes:
        key_length (int): The length of the longest word, used in radix sort.
    """
    def __init__(self):
        """
        Initializes a radix sort-based lexicon.
        """
        super().__init__(sorting_method=radix_sort)
        self.key_length: int = 0

    def insert_element(self, data: str):
        """
        Inserts a word into the lexicon, updating the key length if necessary.

        Args:
            data (str): The word to insert.
        """
        len_data = len(data)
        if len_data > self.key_length:
            self.key_length = len_data

        return super().insert_element(data)

    def sort_dictionary(self):
        """
        Sorts the dictionary keys using radix sort and updates the sorted list.
        """
        keys: list[str] = list(self.dictionary.keys())
        keys = self.sorting_method(keys, self.key_length)
        self.sorted_list = [self.dictionary[word] for word in keys]
