from src.shared.word import Word
import src.utils.neighbours_utils as nb_utils
"""
This module implements `add_neighbours` method for one letter words.

Maintains uniformity with other `add_neighbours` methods.
"""

def add_neighbours(one_char_words: list[Word]):
    """
    Finds and adds neighbors for words of length one. 

    Does nothing if there are no words of length one.
    """
    nb_utils.compare_words_same_list(one_char_words)