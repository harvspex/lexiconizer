from lexiconizer.shared.word import Word
from lexiconizer.utils.neighbours_utils import word_is_neighbours

def test_word_is_neighbours():
    """
    Tests the `word_is_neighbours` function with a set of neighbor and non-neighbor words.

    This function validates that the `word_is_neighbours` utility correctly 
    identifies whether two words are neighbors based on predefined criteria.
    Neighbor words are expected to return `True`, while non-neighbor words 
    should return `False`.

    Test cases:
        - Neighbor words for 'cat': 'bat', 'cut', 'cab'
        - Non-neighbor words for 'cat': 'cup', 'but', 'bag', 'dog'

    Raises:
        AssertionError: If the `word_is_neighbours` function produces 
            incorrect results.
    """
    get_word_list = lambda word_list: [Word(word) for word in word_list.split()]

    test_word = Word('cat')
    neighbour_words = 'bat cut cab'
    non_neighbour_words = 'cup but bag dog'

    for other_word in get_word_list(neighbour_words):
        assert word_is_neighbours(test_word, other_word)

    for other_word in get_word_list(non_neighbour_words):
        assert not word_is_neighbours(test_word, other_word)

def main():
    test_word_is_neighbours()

if __name__ == '__main__':
    main()