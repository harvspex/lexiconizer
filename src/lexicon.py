from word_tree import WordTree, Word
from typing import Callable

# NOTE: staticmethods may be slower. Do testing.
# TODO: init with filename, and run build_lexicon on init?
# TODO: Could add option to time build_lexicon subtasks individually
# TODO: Finish adding type hints

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

                    if data:
                        self.word_tree.insert_element(data)

    def write_to_file(self, filename):
        with open(filename, 'w') as outfile:
            for i in self.sorted_list:
                outfile.write(str(i))

    def add_neighbours_one_char(self):
        # TODO: Check for 1 char neighbours thusly: combine all chars into a single list, then call the check
        # TODO: Add error handling for insufficient lists
        one_char_list = self.same_char_0[0]
        Lexicon.compare_words_different_lists(one_char_list, one_char_mode=True)

    def add_neighbours_same_char_0(self):
        # TODO: Add error handling for insufficient lists
        same_char_0 = self.same_char_0[1:]
        Lexicon.recursive_explore(same_char_0, mode=0, target_level=2)

    def add_neighbours_same_char_1(self):
        Lexicon.recursive_explore(self.same_char_1, mode=1, target_level=2)

    def add_all_neighbours(self):
        self.add_neighbours_one_char()
        self.add_neighbours_same_char_0()
        self.add_neighbours_same_char_1()

    @staticmethod
    def recursive_explore(nested_list: list, mode: int, target_level: int, level: int=0):
        # TODO: Could use a bit of refactoring

        if level == target_level:
            match mode:
                case 0:
                    Lexicon.compare_words_same_list(nested_list)
                case 1:
                    Lexicon.compare_words_different_lists(nested_list)
                case _:
                    # TODO: Raise error
                    return

        # This shouldn't happen
        elif level < 0 or level > target_level:
            return
    
        elif level < target_level:
            for sublist in nested_list:
                Lexicon.recursive_explore(sublist, mode, target_level, level+1)

    @staticmethod
    def compare_words_same_list(inner_list: list[Word], start: int=0, end: int=None):
        """Compares word at inner_list[start] to words in inner_list[start+1:end].
        If words are neighbours, add neighbours to each word."""

        if end is None:
            end = len(inner_list)

        if end == 1:
            return

        for a in range(start, end):
            word_a = inner_list[a]

            for b in range(a+1, end):
                word_b = inner_list[b]

                # TODO: Check len(word_a) impact on runtime
                if Lexicon.word_is_neighbours(word_a, word_b, start=1):
                    Lexicon.add_mutual_neighbours(word_a, word_b, inserting=False)

    @staticmethod
    def yield_lists(nested_list: list, start: int=0, end: int=None, recursive=True):
        if end is None: end = len(nested_list)

        for list_idx in range(start, end):
            for word in nested_list[list_idx]:
                if recursive:
                    yield word, Lexicon.yield_lists(nested_list, list_idx+1, end, recursive=False)
                else:
                    yield word

    @staticmethod
    def compare_words_different_lists(nested_list: list, one_char_mode: bool=False):
        for word_a, other_words in Lexicon.yield_lists(nested_list):
            for word_b in other_words:

                if one_char_mode:
                    Lexicon.add_mutual_neighbours(word_a, word_b, inserting=False)

                elif Lexicon.word_is_neighbours(word_a, word_b, start=2, end=len(word_a.spelling), diffs=1):
                    Lexicon.add_mutual_neighbours(word_a, word_b, inserting=True)

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
    def add_mutual_neighbours(word_a: Word, word_b: Word, inserting: bool=False):
        # NOTE: This will have to be modified for same_char_1 words, because words will be inserted
        # to word_b's neighbour list (not appended)
        word_a.neighbours.append(word_b.spelling)

        if inserting:
            # TODO: This doesn't always insert in order
            word_b.neighbours.insert(word_b.pointer, word_a.spelling)
            word_b.pointer += 1

        else:
            word_b.neighbours.append(word_a.spelling)

    def reset(self):
        self.word_tree = WordTree()
        self.sorted_list.clear()
        self.same_char_0.clear()
        self.same_char_1.clear()

    def build_lexicon(self, input_filename, output_filename='out.txt', reset=True):

        if reset: self.reset()

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

        print('Finished!\n')
