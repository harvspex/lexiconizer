from typing import Callable
from word_tree import Word

class Lexicon:
    @staticmethod
    def OLD_add_neighbours_same_char_1(nested_list):
        for same_len in nested_list: # Words of same len
            for same_1 in same_len: # Words with same char at index 1
                for list_a_idx in range(len(same_1)):
                    for word_a in same_1[list_a_idx]:
                        for list_b_idx in range(list_a_idx+1, len(same_1)):
                            for word_b in same_1[list_b_idx]:
                                print(f'{word_a.spelling} {word_b.spelling}')

    @staticmethod
    def recursive_explore(nested_list: list, target_level: int, level: int=0):
        # TODO: Could use a bit of refactoring

        if level == target_level:
            Lexicon.compare_words(nested_list)

        # This shouldn't happen
        elif level < 0 or level > target_level:
            return
    
        elif level < target_level:
            for sublist in nested_list:
                Lexicon.recursive_explore(sublist, target_level, level+1)

    @staticmethod
    def compare_words(nested_list: list):
        for list_a_idx in range(len(nested_list)):
            for word_a in nested_list[list_a_idx]:
                for list_b_idx in range(list_a_idx+1, len(nested_list)):
                    for word_b in nested_list[list_b_idx]:
                        print(f'Word a: {word_a.spelling} Word b: {word_b.spelling}')

    @staticmethod
    def add_neighbours_same_char_1(nested_list):
        Lexicon.recursive_explore(nested_list, 2) # 2 ???