from lexiconizer.lexicons.lexicon_dict import LexiconDict
from lexiconizer.sorting.radix_sort import radix_sort

class LexiconRadix(LexiconDict):
    def __init__(self):
        super().__init__(sorting_method=radix_sort)
        self.key_length: int = 0

    def insert_element(self, data: str):
        len_data = len(data)
        if len_data > self.key_length:
            self.key_length = len_data

        return super().insert_element(data)

    def sort_dictionary(self):
        keys: list[str] = list(self.dictionary.keys())
        keys = self.sorting_method(keys, self.key_length)
        self.sorted_list = [self.dictionary[word] for word in keys]
