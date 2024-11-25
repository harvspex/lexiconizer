from dataclasses import dataclass
from word_tree import WordTree, Word
from typing import Callable

# TODO: For all "neighbours" functions, take out exctract loops into common function/s
# Check for 1 char neighbours thusly: combine all chars into a single list, then call the check
# neighbours map method (used in map_to_nested_list) directly on that list

@dataclass
class Lexicon:
    word_tree = WordTree()
    sorted_list: list[Word]
    same_char_0: list[Word] # Could potentially be list[str]
    same_char_1: list[Word] # Could potentially be list[str]
    # Add list for one char words?

    # NOTE: It may be possible to get rid of same_char_0. This would save some memory, but
    # complicate checking same_char_0 slightly

    def read_data(self, filename):
        # Reads data and inserts into Lexicon AVLTree

        with open(filename, 'r') as infile:
            for line in infile:
                tokens = line.lower().strip().split()

                for token in tokens:
                    data = ''.join(c for c in token if c.isalpha())

                    if data:
                        self.word_tree.insert_element(data)

    def map_to_nested_list(self, nested_list: list, map_function: Callable,
                           start: int=0, end: int=None):

        if end is None: end = len(nested_list)

        for i in range(start, end):
            element = nested_list[i]

            if isinstance(element, list):
                self.map_to_nested_list(element, map_function)

            else:
                nested_list[i] = map_function(nested_list, i, end)

    def check_neighbours(inner_list: list[Word], start: int, end: int):
        # TODO: Complete
        word = inner_list[start]

        for i in range(start+1, end):
            # If word is neighbours:
            #   add_mutual_neighbours()
            pass

    def word_is_neighbours(word_a, word_b, start, end, diffs=0):
        """Returns True if words are neighbours, otherwise False.
        Only checks indices between start and end."""

        for i in range(start, end):

            if word_a[i] != word_b[i]:
                diffs += 1

                if diffs > 1:
                    return False

        return True

    def add_mutual_neighbours(word_a: Word, word_b: Word):
        word_a.add_neighbour(word_b)
        word_b.add_neighbour(word_a)

    def add_all_neighbours(self):
        self.add_neighbours_one_char()
        self.add_neighbours_same_char_0()
        self.add_neighbours_same_char_1()

    def add_neighbours_one_char():
        pass

    def add_neighbours_same_char_0():
        pass

    def add_neighbours_same_char_1():
        pass

    def write_to_file(self, sorted_lst, filename):
        with open(filename, 'w') as outfile:
            for i in sorted_lst:
                outfile.write(str(i))

    def build_lexicon(self, input_filename, output_filename):
        # Generate AVL Tree
        self.read_data(input_filename)

        # Populate lists
        self.word_tree.traverse_inorder(self.word_tree.root, self.sorted_list, 
                                           self.same_char_0, self.same_char_1)

        # Add neighbours
        self.add_all_neighbours()

        # Write to file
        self.write_to_file(self.sorted_list, output_filename)
