from lexicons.lexicon_dict import LexiconDict
from utils.quick_sort import quick_sort

class LexiconQuick(LexiconDict):
    def sort_dictionary(self):
        sorted_keys = list(self.dictionary.keys())
        quick_sort(sorted_keys)
        self.sorted_list = [self.dictionary[word] for word in sorted_keys]