from typing import Callable
from word_tree import Word

# TODO: Problems:
#   - Not all neighbours are added
#   - Neighbours not added in order            

class Lexicon:
    # @staticmethod
    # def OLD_add_neighbours_same_char_1(nested_list):
    #     for same_len in nested_list: # Words of same len
    #         for same_1 in same_len: # Words with same char at index 1
    #             for list_a_idx in range(len(same_1)):
    #                 for word_a in same_1[list_a_idx]:
    #                     for list_b_idx in range(list_a_idx+1, len(same_1)):
    #                         for word_b in same_1[list_b_idx]:
    #                             print(f'{word_a.spelling} {word_b.spelling}')

    @staticmethod
    def recursive_explore(nested_list: list, target_level: int, level: int=0, char_0_mode: bool=True):
        # TODO: Could use a bit of refactoring

        if level == target_level:
            if char_0_mode:
                Lexicon.compare_words_char_0(nested_list)
            else:
                Lexicon.compare_words_char_1(nested_list)

        # This shouldn't happen
        elif level < 0 or level > target_level:
            return
    
        elif level < target_level:
            for sublist in nested_list:
                Lexicon.recursive_explore(sublist, target_level, level+1, char_0_mode)

    @staticmethod
    def compare_words_char_1_helper(nested_list: list, start: int=0, end: int=None, recursive=True):
        if end is None: end = len(nested_list)

        for list_idx in range(start, end):
            for word in nested_list[list_idx]:
                if recursive:
                    yield word, Lexicon.compare_words_char_1_helper(nested_list, list_idx+1, end, recursive=False)
                else:
                    yield word

    @staticmethod
    def compare_words_char_1(nested_list: list):
        for word_a, other_words in Lexicon.compare_words_char_1_helper(nested_list):
            # print(f'A: {word_a.spelling}')
            for word_b in other_words:

                # print(f'B: {_.spelling}')
                # TODO: This is where is_neighbour() is called

                if Lexicon.word_is_neighbours(word_a, word_b, start=2, end=len(word_a.spelling), diffs=1):
                    Lexicon.add_mutual_neighbours(word_a, word_b)

    @staticmethod
    def compare_words_char_0(inner_list: list[Word], start: int=0, end: int=None):
        """Compares word at inner_list[start] to words in inner_list[start+1:end].
        If words are neighbours, add neighbours to each word."""

        if end is None:
            end = len(inner_list)

        if end == 1:
            return

        for a in range(start, end):
            word_a = inner_list[a]

            for b in range(a+1, end):
                word_b = inner_list[b]

                # TODO: Check len(word_a) impact on runtime
                if Lexicon.word_is_neighbours(word_a, word_b, start=1):
                    Lexicon.add_mutual_neighbours(word_a, word_b)

    @staticmethod
    def add_neighbours_same_char_1(nested_list):
        Lexicon.recursive_explore(nested_list, 2, char_0_mode=False)

    @staticmethod
    def add_neighbours_same_char_0(nested_list):
        # TODO: This doesn't work
        # Probably easiest to make another (or reuse) compare_words method for same 0
        # Then change recursive_explore to behave differently based on same0 or same1
        Lexicon.recursive_explore(nested_list[1:], 2, char_0_mode=True)

    @staticmethod
    def word_is_neighbours(word_a: Word, word_b: Word, start: int=0, end: int=None, diffs: int=0):
        """Returns True if words are neighbours, otherwise False.
        Only checks letter indices between start and end."""
        spelling_a = word_a.spelling
        spelling_b = word_b.spelling

        if end is None: end = len(spelling_a)

        for i in range(start, end):

            if spelling_a[i] != spelling_b[i]:
                diffs += 1

                if diffs > 1:
                    return False

        return True

    @staticmethod
    def add_mutual_neighbours(word_a: Word, word_b: Word, inserting: bool=False):
        # NOTE: This will have to be modified for same_char_1 words, because words will be inserted
        # to word_b's neighbour list (not appended)
        word_a.neighbours.append(word_b.spelling)

        if inserting:
            # TODO: This doesn't always insert in order
            word_b.neighbours.insert(word_b.pointer, word_a.spelling)
            word_b.pointer += 1

        else:
            word_b.neighbours.append(word_a.spelling)
