import lexiconizer.utils.neighbours_utils as nb_utils
from lexiconizer.lexicons.lexicon_dict import LexiconDict
from lexiconizer.shared.word import Word

# TODO: Docstrings

class LexiconBenchmark(LexiconDict):
    """
    A dictionary-based lexicon used to benchmark neighbour optimisations.

    This subclass omits neighbor finding optimisations, and focuses on
    sorting and other basic operations for benchmarking purposes.
    """
    def __init__(self):
        """
        Initializes a benchmark lexicon.
        """
        super().__init__()

    def populate_lists(self):
        """
        Populates internal lists, focusing only on sorting for benchmarks.
        """
        return super().sort_dictionary()

    @staticmethod
    def chars_match(spelling_a: str, spelling_b: str, index: int):
        """
        Checks if the characters at a specific index match between two strings.

        Args:
            spelling_a (str): The first string.
            spelling_b (str): The second string.
            index (int): The index to compare.

        Returns:
            bool: True if the characters match, False otherwise.
        """
        return spelling_a[index] == spelling_b[index]

    @staticmethod
    def is_neighbours_candidate(word_a: Word, word_b: Word) -> bool:
        """
        Determines if two words are candidates to be neighbors.

        Args:
            word_a (Word): The first word.
            word_b (Word): The second word.

        Returns:
            bool: True if the words are neighbors, False otherwise.
        """
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
        """
        Determines if two words are neighbors.

        Args:
            word_a (Word): The first word.
            word_b (Word): The second word.

        Returns:
            bool: True if the words are neighbors, False otherwise.
        """
        if LexiconBenchmark.is_neighbours_candidate(word_a, word_b):
            return nb_utils.word_is_neighbours(word_a, word_b)
        return False

    def add_all_neighbours(self):
        """
        Adds all neighboring words in the sorted list.
        """
        len_sorted: int = len(self.sorted_list)

        for a in range (len_sorted):
            word_a = self.sorted_list[a]

            for b in range(a+1, len_sorted):
                word_b = self.sorted_list[b]

                if LexiconBenchmark.word_is_neighbours(word_a, word_b):
                    nb_utils.add_mutual_neighbours(word_a, word_b)
