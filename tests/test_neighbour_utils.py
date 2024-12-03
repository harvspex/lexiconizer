from shared.word import Word
from utils.neighbours_utils import word_is_neighbours

def test_word_is_neighbours():
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