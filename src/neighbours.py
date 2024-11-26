from typing import Callable
from word_tree import Word

class Lexicon:
    @staticmethod
    def add_neighbours_same_char_1(nested_list):
        for same_len in nested_list: # Words of same len
            for same_1 in same_len: # Words with same char at index 1
                for list_a_idx in range(len(same_1)):
                    for word_a in same_1[list_a_idx]:
                        for list_b_idx in range(list_a_idx+1, len(same_1)):
                            for word_b in same_1[list_b_idx]:
                                print(f'{word_a.spelling} {word_b.spelling}')

    @staticmethod
    def dig_into_sublist(nested_list: list, *args, start: int=0, end: int=None):
        if end is None: end = len(nested_list)

        for i in range(start, end):
            element = nested_list[i]
            args[0](element, args[1:])
