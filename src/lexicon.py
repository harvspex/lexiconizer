from word_tree import WordTree, Word
from typing import Callable

# NOTE: staticmethods may be slower. Do testing.
# TODO: init with filename, and run build_lexicon on init?
# TODO: Could add option to time build_lexicon subtasks individually

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
        """Explores nested lists. When a non-list element is found, applies map_function to element.
        Only checks indices between start and end."""

        if end is None: end = len(nested_list)

        for i in range(start, end):
            element = nested_list[i]

            # Could have something like:
            #
            # if max_nesting_depth:
            #   max_nesting_depth -= 1
            #
            #   if max_nesting_depth == 0:
            #       ...

            if isinstance(element, list):
                Lexicon.map_to_nested_list(element, map_function)

            else:
                map_function(nested_list, i, end)

    # NOTE: As-is, this only compares words within the same list. For checking same idx 1
    # neighbours, the comparisons occur between sublists at different nesting depths.
    #
    # e.g.:
    # for word_a in same_1:
    #     for word_b in same_0: (starting after word_a)
    #         compare(word_a, word_b)
    #
    # Possible solution part 1:
    # - Make map_to_nested() stop at a certain nesting depth (or when sublist contains non-sublists)
    # - Make another version of check_neighbours() that checks all words in sublist A against all
    #   all words in sublist B, C, D... N
    # - New check_neighbours() should operate on sublists containing words (not words directly)
    #
    # Possible solution part 2:
    # Don't call add_mutual_neighbours. Pass in a map function as an argument.
    #
    # For same 0, pass in:
    # def map_fun():
    #    if word is neighbours():
    #       add_mutual_neighbours()
    #
    # For same 1, pass in a function that iterates through sublists as required, then makes
    # comparisons on the words within
    #
    # NOTE: This is a map function
    @staticmethod
    def check_neighbours(inner_list: list[Word], start: int, end: int):
        """Compares word at inner_list[start] to words in inner_list[start+1:end].
        If words are neighbours, add neighbours to each word."""
        word_a = inner_list[start]

        for i in range(start+1, end):
            word_b = inner_list[i]

            if Lexicon.word_is_neighbours(word_a, word_b, 1, len(word_a.spelling)):
                Lexicon.add_mutual_neighbours(word_a, word_b)

                # TODO: Refactor so this can work with same_1
                # TODO: Check len(word_a) impact on runtime

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
        word_a.neighbours.append(word_b.spelling)
        word_b.neighbours.append(word_a.spelling)

    def add_all_neighbours(self):
        # Lexicon.add_neighbours_one_char()
        # Lexicon.add_neighbours_same_char_0(self)
        # Lexicon.add_neighbours_same_char_1()

        # Testing with methods from neighbours.py
        from neighbours import Lexicon as L
        print('Same 0')
        L.add_neighbours_same_char_0(self.same_char_0)

        print('Same 1')
        L.add_neighbours_same_char_1(self.same_char_1)

    def add_neighbours_one_char(self):
        # TODO: Check for 1 char neighbours thusly: combine all chars into a single list, then call the check
        pass

    def add_neighbours_same_char_0(self):
        Lexicon.map_to_nested_list(self.same_char_0, self.check_neighbours, start=1)

    def add_neighbours_same_char_1(self):
        pass

    def write_to_file(self, filename):
        with open(filename, 'w') as outfile:
            for i in self.sorted_list:
                outfile.write(str(i))

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
