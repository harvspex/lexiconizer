from typing import Callable
from word_tree import Word

class Lexicon:
    @staticmethod
    def map_to_nested_list(nested_list: list, map_function: Callable, max_nesting_depth:int=None,
                            start: int=0, end: int=None):
        """Explores nested lists. When a non-list element is found, applies map_function to element.
        Only checks indices between start and end."""

        if end is None: end = len(nested_list)

        for i in range(start, end):
            element = nested_list[i]

            if max_nesting_depth:
                max_nesting_depth -= 1
            
                if max_nesting_depth == 0:
                    map_function(element, start+1, end)

            # elif isinstance(element, list):
            #     Lexicon.map_to_nested_list(element, map_function)

            # else:
            #     map_function(nested_list, i, end)

    @staticmethod
    def check_neighbours(inner_list: list[Word], start: int, end: int):
        """Compares word at inner_list[start] to words in inner_list[start+1:end].
        If words are neighbours, add neighbours to each word."""

        print(f'Start: {start} End: {end} len(inner_list): {len(inner_list)}')

        item_a = inner_list[start]

        for i in range(start+1, end):
            item_b = inner_list[i]

            for word_a in item_a:
                for word_b in item_b:
                    print(f'{word_a.spelling} {word_b.spelling}')

    @staticmethod
    def add_neighbours_same_char_1(nested_list):
        Lexicon.map_to_nested_list(nested_list, Lexicon.check_neighbours, max_nesting_depth=3)

    @staticmethod
    def word_is_neighbours(): pass

    @staticmethod
    def add_mutual_neighbours(): pass