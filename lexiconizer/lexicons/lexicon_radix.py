from lexicons.lexicon_dict import LexiconDict
from utils.radix_sort import radix_sort

class LexiconRadix(LexiconDict):
    def sort_dictionary(self):
        sorted_keys = list(self.dictionary.keys())
        sorted_keys = radix_sort(sorted_keys)
        self.sorted_list = [self.dictionary[word] for word in sorted_keys]