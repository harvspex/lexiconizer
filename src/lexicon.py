from word_tree import WordTree, Word
from typing import Callable

class Lexicon:
    def __init__(self):
        self.word_tree = WordTree()
        self.sorted_list: list[Word] = []
        self.same_char_0: list[Word] = [] # Could potentially be list[str]
        self.same_char_1: list[Word] = [] # Could potentially be list[str]
        # Add list for one char words?

    # NOTE: It may be possible to get rid of same_char_0. This would save some memory, but
    # complicate checking same_char_0 slightly

    def read_data(self, filename):
        """Reads text data from filename and inserts into Lexicon AVLTree"""

        with open(filename, 'r') as infile:
            for line in infile:
                tokens = line.lower().strip().split()

                for token in tokens:
                    data = ''.join(c for c in token if c.isalpha())
                    if data: self.word_tree.insert_element(data)

    @staticmethod
    def map_to_nested_list(nested_list: list, map_function: Callable,
                           start: int=0, end: int=None):
        """Explores nested lists. When a non-list element is found, applies map_function to element."""

        if end is None: end = len(nested_list)

        for i in range(start, end):
            element = nested_list[i]

            if isinstance(element, list):
                Lexicon.map_to_nested_list(element, map_function)

            else:
                nested_list[i] = map_function(nested_list, i, end)

    @staticmethod
    def check_neighbours(inner_list: list[Word], start: int, end: int):
        """Compares word at inner_list[start] to words in inner_list[start+1:end].
        If words are neighbours, add neighbours to each word."""

        # TODO: Complete. This is the map_function that will be passed to map_to_nested_list
        word_a = inner_list[start]

        for i in range(start+1, end):
            word_b = inner_list[i]
            if Lexicon.word_is_neighbours(word_a, word_b, 1, len(word_a)):
                # TODO: Check len(word_a) impact on runtime
                # Refactor so this can work with same_1
                Lexicon.add_mutual_neighbours(word_a, word_b)

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
    def add_mutual_neighbours(word_a: Word, word_b: Word):
        # NOTE: This will have to be modified for same_char_1 words, because words will be inserted
        # to word_b's neighbour list (not appended)
        word_a.add_neighbour(word_b)
        word_b.add_neighbour(word_a)

    @staticmethod
    def add_all_neighbours():
        # Lexicon.add_neighbours_one_char()
        Lexicon.add_neighbours_same_char_0()
        Lexicon.add_neighbours_same_char_1()

    @staticmethod
    def add_neighbours_one_char():
        # TODO: Check for 1 char neighbours thusly: combine all chars into a single list, then call the check
        pass

    @staticmethod
    def add_neighbours_same_char_0():
        pass

    @staticmethod
    def add_neighbours_same_char_1():
        pass

    def write_to_file(self, filename):
        with open(filename, 'w') as outfile:
            for i in self.sorted_list:
                outfile.write(str(i)) # TODO: ensure this works (rather than str(i))

    def build_lexicon(self, input_filename, output_filename='out.txt'):
        print('Reading data...')
        # Generate AVL Tree
        self.read_data(input_filename)

        print('Populating lists...')
        # Populate lists
        self.word_tree.traverse_inorder(self.word_tree.root, self.sorted_list, self.same_char_0, self.same_char_1)

        print('Adding neighbours...')
        # Add neighbours
        self.add_all_neighbours()

        print('Writing to file...')
        # Write to file
        self.write_to_file(output_filename)
