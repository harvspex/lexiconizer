from src.word_tree import Word
"""
neighbours_utils.py

This module provides utility functions for finding and adding word
neighbors.

The functions in this module are designed to help identify, process, 
and manage neighboring words based on various criteria such as 
character differences, alphabetical order, or word lengths.

Typical Use Cases:
- Identifying words that differ by one character.
- Managing lists of neighboring words.
- Providing helper methods for word-based operations in the WordTree.

Functions:
    is_neighbor(word1: str, word2: str) -> bool
        Determines if two words are neighbors by differing in only one
        character.
    sort_neighbors(neighbors: list[str]) -> list[str]
        Sorts a list of neighbors alphabetically.
    find_neighbors(word: str, word_list: list[str]) -> list[str]
        Finds all neighbors of a given word in a provided word list.
"""

def word_is_neighbours(
    word_a: Word,
    word_b: Word,
    start: int=0,
    end: int=None,
    diffs: int=0
):
    """
    Determines if two words are neighbors based on character 
    differences.

    Args:
        word_a (Word): The first word.
        word_b (Word): The second word.
        start (int): The starting index for comparison (default: 0).
        end (int): The ending index for comparison (default: None,
            meaning the length of the word).
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
    Adds two words as mutual neighbors in their respective neighbor 
    lists.

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
        end (int): The ending index for comparison (default: None, 
            meaning the end of the list).

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

            # TODO: Can end be passed into word_is_neighbours based on the
            # index of the current list?

            if word_is_neighbours(word_a, word_b, start=1):
                add_mutual_neighbours(word_a, word_b, inserting=False)
