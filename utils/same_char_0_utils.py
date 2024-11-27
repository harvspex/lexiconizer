import utils.neighbours_utils as nb_utils

def add_neighbours(nested_word_lists: list):
    """
    Identifies and adds neighbors for words sharing the same first character.
    
    Operates on the `nested_word_lists` list.
    """
    compare_same_char_0_words(nested_word_lists)

def compare_same_char_0_words(nested_word_lists: list):
    # TODO: refactor?
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

def yield_same_char_0_list(same_len_list: list, char_0_idx):
    # TODO: Write docstring
    # This takes a list of same_len words
    # It then digs 1 level into each sublist (of same_char_1 words)
    # It then yields a sublist at the specified yield_idx
    # Once no sublists remain, all are yielded

    out_of_range: int = 0

    for same_char_1 in same_len_list:
        try:
            yield same_char_1[char_0_idx]
        except IndexError:
            out_of_range += 1

    if out_of_range == len(same_len_list):
        yield None
