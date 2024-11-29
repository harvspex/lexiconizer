import utils.neighbours_utils as nb_utils

def add_neighbours(nested_word_lists: list):
    """
    Identifies and adds neighbors for words sharing the same first 
    character.

    Operates on the `nested_word_lists` list.
    """
    compare_same_char_0_words(nested_word_lists)

def compare_same_char_0_words(nested_word_lists: list):
    """
    Compares words with same char 0 (i.e. same first letter) to find 
    neighbours.

    Args:
        nested_word_lists (list): A list of words nested by:
            1. Word length
            2. Char 1
            3. Char 0

    This iterates through lists of words with the same length. Sublists 
    of words with same char 0 are yielded using 
    `yield_same_char_0_list`. Once all sublists are yielded, they are 
    combined into one list, and checked using `compare_words_same_list`.
    """
    counter: int = 0

    for same_len_list in nested_word_lists:
        counter = 0

        while True:
            lists = yield_same_char_0_list(same_len_list, counter)
            combined = []

            try:
                for sublist in lists:
                    combined += sublist
            except TypeError:
                break

            nb_utils.compare_words_same_list(combined)
            counter += 1

def yield_same_char_0_list(same_len_list: list, char_0_idx: int):
    """
    Yields lists of words with same length and same first letter, to be 
    used for checking neighbours.

    This works by:
        1. Iterating through each of words with same char at index 1
        2. Yielding a sublist of words with the same char at index 0 
           (at char_0_idx)
        3. If no lists contain a sublist at char_0_idx (i.e. all 
           sublists are yielded), yields only None to denote end of 
           same_len_list.

    Args:
        same_len_list (list): Nested list ultimately containing words of
            the same length.
        char_0_idx (int): Nested list index corresponding to the current
            first letter.

    Yields:
        A generator containing sublists.
    """
    out_of_range: int = 0

    for same_char_1 in same_len_list:
        try:
            yield same_char_1[char_0_idx]
        except IndexError:
            out_of_range += 1

    if out_of_range == len(same_len_list):
        yield None
