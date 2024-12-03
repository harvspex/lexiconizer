import src.utils.neighbours_utils as nb_utils
from src.lexicon.lexicon_dict import LexiconDict
from src.shared.word import Word

# TODO: Docstrings

class LexiconBenchmark(LexiconDict):
    def __init__(self):
        super().__init__()

    def populate_lists(self):
        return super().sort_dictionary()

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

    def add_all_neighbours(self):
        len_sorted: int = len(self.sorted_list)

        for a in range (len_sorted):
            word_a = self.sorted_list[a]

            for b in range(a+1, len_sorted):
                word_b = self.sorted_list[b]

                if LexiconBenchmark.word_is_neighbours(word_a, word_b):
                    nb_utils.add_mutual_neighbours(word_a, word_b)
