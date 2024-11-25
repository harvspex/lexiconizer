from dataclasses import dataclass
from lexicon_tree import LexiconTree, Word
from typing import Callable

# TODO: For all "neighbours" functions, take out exctract loops into common function/s

@dataclass
class Lexicon:
    lexicon_tree: LexiconTree
    sorted_list: list[Word]
    same_char_0: list[Word] # Could potentially be list[str]
    same_char_1: list[Word] # Could potentially be list[str]

    def read_data(self, filename):
    # Reads data and inserts into AVLTree, or increments frequencyuency if data already present.
        with open(filename, 'r') as infile:
            for line in infile:
                tokens = line.lower().strip().split()

                for token in tokens:
                    data = ''.join(ch for ch in token if ch.isalpha())

                    if data:
                        self.lexicon_tree.insert_element(data)

    # Returns True if words are neighbours, otherwise False.
    # Only checks indices between start and end.
    def check_neighbours(word_1, word_2, start, end, diffs=0):
        for i in range(start, end):

            if word_1[i] != word_2[i]:
                diffs += 1

                if diffs > 1:
                    return False

        return True

    #         Adds neighbours for words with only one char.
    #         check_neighbours() not required as all one-char words are neighbours (other than self).
    def neighbours_one_char(one_char):
        len_one_char = len(one_char)

        for i in range (len_one_char):
            for a in one_char[i]: # Word 1
                spelling_1 = a.spelling
                neighbours_1 = a.neighbours

                for j in range(i+1, len_one_char):
                    for b in one_char[j]: # Word 2
                        spelling_2 = b.spelling
                        neighbours_2 = b.neighbours

                        neighbours_1.append(spelling_2)
                        neighbours_2.append(spelling_1)

    #         Adds neighbours for words of same length and with same first letter.
    #         check_neighbours() begins after first letter, as it is always the same.
    def neighbours_same_0(same_0):
        for same_len in range(len(same_0)): # Words of same length

            for inner in same_0[same_len]: # Words with same char at idx 0
                len_inner = len(inner)
                if len_inner > 1:

                    for i in range(len_inner): # Word 1
                        spelling_1 = inner[i].spelling
                        neighbours_1 = inner[i].neighbours

                        for j in range(i+1, len_inner): # Word 2
                            spelling_2 = inner[j].spelling
                            neighbours_2 = inner[j].neighbours

                            if check_neighbours(spelling_1, spelling_2, 1, same_len+1):
                                neighbours_1.append(spelling_2)
                                neighbours_2.append(spelling_1)

    # Adds neighbours for words of same length and with same second letter.
    # SKIPS words with same first letter (checked previously).

    # check_neighbours() begins after second letter, with 1 difference already counted.
    # (First letter always different, second letter always same.)

    # spelling_1 inserted to neighbours_2 BEFORE all neighbours previously added in neighbours_same_0(),
    # and AFTER all neighbours previously added in neighbours_same_1(). Word.pointer keeps count of this
    # index for each Word object.
    def neighbours_same_1(same_1):
        for same_len in range(len(same_1)): # Words of same length

            for lst in same_1[same_len]: # Words with same char at idx 1
                len_lst = len(lst)

                for a in range(len_lst): # Words with same char at idx 0

                    for b in range(len(lst[a])): # Word 1
                        word_1 = lst[a][b]
                        spelling_1 = word_1.spelling
                        neighbours_1 = word_1.neighbours

                        for c in range(a+1, len_lst): # Words with same char at idx 0, starting AFTER Word 1

                            for d in range(len(lst[c])): # Word 2
                                word_2 = lst[c][d]
                                spelling_2 = word_2.spelling
                                neighbours_2 = word_2.neighbours

                                if check_neighbours(spelling_1, spelling_2, 2, same_len+1, 1):
                                    neighbours_1.append(spelling_2)
                                    neighbours_2.insert(word_2.pointer, spelling_1)
                                    word_2.pointer += 1

    def write_to_file(sorted_lst, filename):
        with open(filename, 'w') as outfile:
            for i in sorted_lst:
                outfile.write(str(i))

    def build_lexicon(input_filename, output_filename):
        lexicon = AVLTree()
        sorted_lst, same_0, same_1 = [], [], []

        # Generate AVL Tree
        read_data(lexicon, input_filename)

        # Populate lists
        lexicon.traverse_inorder(lexicon.root, sorted_lst, same_0, same_1)

        # Add neighbours
        neighbours_one_char(same_0[0])
        neighbours_same_0(same_0)
        neighbours_same_1(same_1)

        # Write to file
        write_to_file(sorted_lst, output_filename)