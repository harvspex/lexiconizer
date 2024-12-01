from src.lexicon.lexicon_dict import LexiconDict
from src.shared.func_class import FuncClass
from src.shared.word import Word
import src.utils.neighbours_utils as neighbour_utils

# TODO: Docstrings

class LexiconBenchmark(LexiconDict):
    def __init__(self, slow_mode: int=False):
        super().__init__()
        self.slow_mode = slow_mode

    def get_build_lexicon_funcs(self, input_filename: str, output_filename: str):
        funcs = [
            FuncClass(self.read_data, 'Reading and inserting data...', input_filename),
            FuncClass(self.sort_dictionary, 'Sorting lexicon...'),
            FuncClass(self.add_all_neighbours, 'Adding neighbours...', self.slow_mode),
            FuncClass(self.write_to_file, 'Writing to file...', output_filename)
        ]
        return funcs

    @staticmethod
    def chars_match(spelling_a: str, spelling_b: str, index: int):
        return spelling_a[index] == spelling_b[index]

    @staticmethod
    def is_neighbours_candidate(word_a: Word, word_b: Word) -> bool:
        spelling_a = word_a.spelling
        spelling_b = word_b.spelling

        if len(spelling_a) != len(spelling_b):
            return False

        elif len(spelling_a) == 1:
            return True

        return (
            LexiconBenchmark.chars_match(spelling_a, spelling_b, index=0)
            or LexiconBenchmark.chars_match(spelling_a, spelling_b, index=1)
        )

    @staticmethod
    def word_is_neighbours(word_a: Word, word_b: Word):
        if LexiconBenchmark.is_neighbours_candidate(word_a, word_b):
            return neighbour_utils.word_is_neighbours(word_a, word_b)
        return False

    @staticmethod
    def add_mutual_neighbours(word_a: Word, word_b: Word):
        word_a.neighbours.append(word_b.spelling)
        word_b.neighbours.append(word_a.spelling)

    def add_all_neighbours(self, slow_mode: int=False):
        if slow_mode: self.add_all_neighbours_slow()
        else: self.add_all_neighbours_fast()

    def add_all_neighbours_fast(self):
        keys = list(self.dictionary.keys())
        len_keys = len(keys)

        for a in range(len_keys):
            spelling_a = keys[a]
            word_a = self.dictionary[spelling_a]

            for b in range(a+1, len_keys):
                spelling_b = keys[b]
                word_b = self.dictionary[spelling_b]

                if LexiconBenchmark.word_is_neighbours(word_a, word_b):
                    LexiconBenchmark.add_mutual_neighbours(word_a, word_b)

    def add_all_neighbours_slow(self):
        word_list: list[Word] = list(self.dictionary.values())
        for word_a in word_list:
            for word_b in word_list:
                if LexiconBenchmark.word_is_neighbours(word_a, word_b):
                    word_a.neighbours.append(word_b.spelling)
