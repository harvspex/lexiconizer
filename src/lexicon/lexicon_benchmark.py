from src.lexicon.lexicon_dict import LexiconDict
from src.shared.func_class import FuncClass
from src.shared.word import Word
import src.utils.neighbours_utils as nb_utils

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
            return nb_utils.word_is_neighbours(word_a, word_b)
        return False

    def add_all_neighbours(self, slow_mode: int=False):
        len_sorted: int = len(self.sorted_list)
        b_start: int = 0

        print(f'Slow mode: {slow_mode}')

        for a in range (len_sorted):
            word_a = self.sorted_list[a]

            if not slow_mode:
                b_start = a+1

            for b in range(b_start, len_sorted):
                word_b = self.sorted_list[b]

                if LexiconBenchmark.word_is_neighbours(word_a, word_b):
                    nb_utils.add_mutual_neighbours(word_a, word_b)
