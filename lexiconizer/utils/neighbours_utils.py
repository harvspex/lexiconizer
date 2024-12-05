from typing import Any
from lexiconizer.shared.word import Word
"""
This module provides utility functions for finding and adding neighbors.

The functions in this module help identify, process, and manage 
neighboring words based on various criteria such as character 
differences, alphabetical order, or word lengths.
"""

def word_is_neighbours(
    word_a: Word,
    word_b: Word,
    start: int=0,
    end: int=None,
    diffs: int=0
) -> bool:
    """
    Determines if two words are neighbors based on character differences.

    Args:
        word_a (Word): The first word.
        word_b (Word): The second word.
        start (int): The starting index for comparison (default: 0).
        end (int): The ending index for comparison (default: None, meaning 
            the length of the word).
        diffs (int): The initial number of character differences 
            (default: 0).

    Returns:
        bool: True if the words are neighbors, False otherwise.
    """
    spelling_a = word_a.spelling
    spelling_b = word_b.spelling

    # TODO: Check len(spelling_a) impact on runtime
    if end is None: end = len(spelling_a)

    for i in range(start, end):

        if spelling_a[i] != spelling_b[i]:
            diffs += 1

            if diffs > 1:
                return False

    return True


def add_mutual_neighbours(word_a: Word, word_b: Word, inserting: bool=False):
    """
    Adds two words as mutual neighbors in their respective neighbor lists.

    Args:
        word_a (Word): The first word.
        word_b (Word): The second word.
        inserting (bool): Whether to insert word_b's neighbor into a 
            specific position (default: False).
    """
    word_a.neighbours.append(word_b.spelling)

    if inserting:
        word_b.neighbours.insert(word_b.pointer, word_a.spelling)
        word_b.pointer += 1

    else:
        word_b.neighbours.append(word_a.spelling)


def compare_words_same_list(word_list: list[Word], start: int=0, end: int=None):
    """
    Compares words in the same list to find neighbors.

    Args:
        inner_list (list[Word]): The list of words to compare.
        start (int): The starting index for comparison (default: 0).
        end (int): The ending index for comparison (default: None, meaning 
            the end of the list).

    Adds mutual neighbors for each word that matches criteria.
    """
    if end is None:
        end = len(word_list)

    if end == 1:
        return

    for a in range(start, end):
        word_a = word_list[a]

        for b in range(a+1, end):
            word_b = word_list[b]

            # TODO: Can end be passed into word_is_neighbours based on the index of the current list?

            if word_is_neighbours(word_a, word_b, start=1):
                add_mutual_neighbours(word_a, word_b, inserting=False)


def add_word_to_nested_list(word: Word, nested_word_list: list, one_char_words: list):
    """
    Adds word to nested list, or to different list if word is one letter.

    Args:
        word (Word): The Word object to add.
        nested_word_list (list): The nested word list
        one_char_words (list): The list of one letter words

    Behavior:
        - Attemps to add word to `nested_word_list`, nested by: length,
          then char 1, then char 0
        - If word is one char, adds to `one_char_words`
    """
    spelling = word.spelling

    try:
        # Add word to nested_word_list
        length = len(spelling) - 1
        i1 = get_index(spelling[1])
        i0 = get_index(spelling[0])
        add_to_nested_list(word, nested_word_list, length, i1, i0)

    except IndexError:
        # If word is one char, add word to one_char_words
        if len(spelling) == 1: # Should always be true
            one_char_words.append(word)


def get_index(c: str) -> int:
    """
    Calculates the alphabetical index of a character relative to 'a'

    Args:
        c (str): A single character.

    Returns:
        int: The index of the character (0 for 'a', 1 for 'b', etc.)
    """
    return ord(c[0]) - ord('a')


def add_to_nested_list(element: Any, lst: list, *n: int):
    """
    Iteratively nests lists at each index in n, appending element to deepest list.

    Args:
        element (Any): The element to add.
        lst (list): The outermost list to which the word will be added.
        *n (int): A sequence of indices specifying the nested structure.

    Behavior:
        - Navigates the nested structure according to the indices in `n`.
        - Creates intermediate lists as needed if they do not exist.
        - Appends the element to the deepest list specified by `n`.
    """
    for i in n:
        try:
            lst = lst[i]

        except IndexError:
            for _ in range(len(lst), i+1):
                lst.append([])
            lst = lst[i]

    lst.append(element)
