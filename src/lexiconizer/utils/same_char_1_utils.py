import lexiconizer.utils.neighbours_utils as nb_utils
"""
Utility functions to add neighbors for words with same second letter (char 1).
"""

def add_neighbours(nested_word_lists: list):
    """
    Finds and adds neighbors for words sharing the same second character.

    Operates on the `nested_word_lists` list.
    """
    TARGET_LEVEL: int  = 2
    recursive_explore(nested_word_lists, target_level=TARGET_LEVEL)

def recursive_explore(nested_list: list, target_level: int, level: int=0):
    """
    Recursively explores a nested list to a specific depth.

    Once target depth is reached, checks for neighbours using 
    `compare_words_different_lists`.

    Args:
        nested_list (list): The list to explore.
        target_level (int): The depth to explore in the nested list.
        level (int): The current depth (default: 0).
    """
    if level == target_level:
        compare_words_different_lists(nested_list)

    # Could be faster but less safe by skipping this elif.
    elif level < target_level:
        for sublist in nested_list:
            recursive_explore(sublist, target_level, level+1)

    # This condition shouldn't happen. Guards against bad `level` value.
    elif level < 0 or level > target_level:
        return


def compare_words_different_lists(nested_list: list):
    """
    Compares words across different lists to find neighbors.

    This compares every word in word_a to every other word in other_words.
    Words within word_a don't need to be compared, as they have been checked
    previously by `same_char_0_utils`.

    Args:
        nested_list (list): The nested list of words.
    """
    # TODO: Can end be passed into word_is_neighbours via the index of the
    # current list?
    for word_a, other_words in yield_lists(nested_list):
        for word_b in other_words:

            if nb_utils.word_is_neighbours(word_a, word_b, start=2, diffs=1):
                nb_utils.add_mutual_neighbours(word_a, word_b, inserting=True)

def yield_lists(nested_list: list, start: int=0, end: int=None, recursive=True):
    # TODO: Reword
    """
    Yields a list and a list generator from a nested list.

    Args:
        nested_list (list): The nested list to process.
        start (int): The starting index (default: 0).
        end (int): The ending index (default: None, meaning the end of the 
            list).
        recursive (bool): Whether to yield recursively through sublists 
            (default: True).

    Yields:
        tuple: A tuple containing:
            - A single sublist
            - A sublist generator
    """
    if end is None: end = len(nested_list)

    for list_idx in range(start, end):
        for word in nested_list[list_idx]:
            if recursive:
                yield word, yield_lists(
                    nested_list,
                    start=list_idx+1,
                    end=end,
                    recursive=False
                )
            else:
                yield word