from lexicons.lexicon_dict import LexiconDict

class LexiconBuiltin(LexiconDict):

    def sort_dictionary(self):
        sorted_keys = list(self.dictionary.keys())
        sorted_keys = sorted(sorted_keys)
        self.sorted_list = [self.dictionary[word] for word in sorted_keys]