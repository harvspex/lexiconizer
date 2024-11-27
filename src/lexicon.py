from word_tree import WordTree, Word

# NOTE: staticmethods may be slower. Do testing.
# TODO: init with filename, and run build_lexicon on init?
# TODO: Could add option to time build_lexicon subtasks individually
# TODO: Finish adding type hints

# TODO: Remove same_chars_0. Replace with list for one_char words

class Lexicon:
    """
    A class for managing a lexicon of words stored in an AVL Tree structure.
    The Lexicon supports reading words from files, finding neighboring words,
    and saving results to an output file.

    # TODO: Edit attributes
    Attributes:
        word_tree (WordTree): The AVL Tree storing words.
        sorted_list (list[Word]): A list of words in sorted order.
        same_char_0 (list[Word]): A list of words that share the same first character.
        same_char_1 (list[Word]): A list of words that share the same second character.
    """

    def __init__(self):
        self.word_tree = WordTree()
        self.sorted_list: list[Word] = []
        self.same_char_0: list[Word] = [] # Could potentially be list[str]
        self.same_char_1: list[Word] = [] # Could potentially be list[str]
        # Add list for one char words?

    # NOTE: It may be possible to get rid of same_char_0. This would save some memory, but
    # complicate checking same_char_0 slightly

    def read_data(self, filename):
        """
        Reads text data from a file and inserts it into the Lexicon's AVL Tree.

        Args:
            filename (str): The path to the input file containing words.

        # TODO: actually raise the error
        Raises:
            IOError: If the file cannot be read.
        """

        with open(filename, 'r') as infile:
            for line in infile:
                tokens = line.lower().strip().split()

                for token in tokens:
                    data = ''.join(c for c in token if c.isalpha())

                    if data:
                        self.word_tree.insert_element(data)

    def write_to_file(self, filename):
        """
        Writes the sorted list of words to a file.

        Args:
            filename (str): The path to the output file where data will be written.

        # TODO: Actually raise the error
        Raises:
            IOError: If the file cannot be written.
        """
        with open(filename, 'w') as outfile:
            for i in self.sorted_list:
                outfile.write(str(i))

    def add_neighbours_one_char(self):
        """
        Finds and adds neighbors for words of length one. 
        Neighbors are identified by specific character differences.
        
        Does nothing if there are no words of length one.
        """

        try:
            one_char_list = self.same_char_0[0]
            Lexicon.compare_words_different_lists(one_char_list, one_char_mode=True)
        except IndexError:
            return

    def add_neighbours_same_char_0(self):
        """
        Identifies and adds neighbors for words sharing the same first character.
        
        Operates on the `same_char_0` list.
        """

        # try:
        #     same_char_0 = self.same_char_0[1:]
        #     Lexicon.recursive_explore(same_char_0, mode=0, target_level=2)
        # except IndexError:
        #     return

        Lexicon.compare_same_0(self.same_char_1)

    def add_neighbours_same_char_1(self):
        """
        Identifies and adds neighbors for words sharing the same second character.
        
        Operates on the `same_char_1` list.
        """

        Lexicon.recursive_explore(self.same_char_1, mode=1, target_level=2)

    def add_all_neighbours(self):
        """
        Executes all neighbor-finding methods, including:
        - `add_neighbours_one_char`
        - `add_neighbours_same_char_0`
        - `add_neighbours_same_char_1`
        """

        self.add_neighbours_one_char()
        self.add_neighbours_same_char_0()
        self.add_neighbours_same_char_1()

    @staticmethod
    def recursive_explore(nested_list: list, mode: int, target_level: int, level: int=0):
        """
        Recursively explores a nested list to a specific depth and processes its contents.

        Args:
            nested_list (list): The list to explore.
            mode (int): The mode of operation (e.g., comparison method).
                - 0: Compare words in the same list.
                - 1: Compare words across different lists.
            target_level (int): The depth to explore in the nested list.
            level (int): The current depth (default: 0).

        Raises:
            ValueError: If an unsupported mode is provided.
        """

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
        """
        Compares words in the same list to find neighbors.

        Args:
            inner_list (list[Word]): The list of words to compare.
            start (int): The starting index for comparison (default: 0).
            end (int): The ending index for comparison (default: None, meaning the end of the list).

        Adds mutual neighbors for each word that matches criteria.
        """

        if end is None:
            end = len(inner_list)

        if end == 1:
            return

        for a in range(start, end):
            word_a = inner_list[a]

            for b in range(a+1, end):
                word_b = inner_list[b]

                if Lexicon.word_is_neighbours(word_a, word_b, start=1):
                    Lexicon.add_mutual_neighbours(word_a, word_b, inserting=False)

    @staticmethod
    def yield_lists(nested_list: list, start: int=0, end: int=None, recursive=True):
        """
        Yields items and their sublists from a nested list. # TODO: Reword

        Args:
            nested_list (list): The nested list to process.
            start (int): The starting index (default: 0).
            end (int): The ending index (default: None, meaning the end of the list).
            recursive (bool): Whether to yield recursively through sublists (default: True).

        Yields:
            tuple: A tuple containing an item and its sublist generator.
        """

        if end is None: end = len(nested_list)

        for list_idx in range(start, end):
            for word in nested_list[list_idx]:
                if recursive:
                    yield word, Lexicon.yield_lists(nested_list, start=list_idx+1, end=end, recursive=False)
                else:
                    yield word

    @staticmethod
    def compare_words_different_lists(nested_list: list, one_char_mode: bool=False):
        """
        Compares words across different lists to find neighbors.

        Args:
            nested_list (list): The nested list of words.
            one_char_mode (bool): Whether to operate in single-character comparison mode.
                                  (default: False)

        Adds mutual neighbors based on comparison criteria.
        """

        for word_a, other_words in Lexicon.yield_lists(nested_list):
            for word_b in other_words:

                if one_char_mode:
                    Lexicon.add_mutual_neighbours(word_a, word_b, inserting=False)

                elif Lexicon.word_is_neighbours(word_a, word_b, start=2, end=len(word_a.spelling), diffs=1):
                    Lexicon.add_mutual_neighbours(word_a, word_b, inserting=True)

    @staticmethod
    def word_is_neighbours(word_a: Word, word_b: Word, start: int=0, end: int=None, diffs: int=0):
        """
        Determines if two words are neighbors based on character differences.

        Args:
            word_a (Word): The first word.
            word_b (Word): The second word.
            start (int): The starting index for comparison (default: 0).
            end (int): The ending index for comparison (default: None, meaning the length of the word).
            diffs (int): The initial number of character differences (default: 0).

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

    @staticmethod
    def add_mutual_neighbours(word_a: Word, word_b: Word, inserting: bool=False):
        """
        Adds two words as mutual neighbors in their respective neighbor lists.

        Args:
            word_a (Word): The first word.
            word_b (Word): The second word.
            inserting (bool): Whether to insert the neighbor into a specific position (default: False).
        """

        word_a.neighbours.append(word_b.spelling)

        if inserting:
            word_b.neighbours.insert(word_b.pointer, word_a.spelling)
            word_b.pointer += 1

        else:
            word_b.neighbours.append(word_a.spelling)

    def reset(self):
        """Resets the lexicon."""
        self.word_tree = WordTree()
        self.sorted_list.clear()
        self.same_char_0.clear()
        self.same_char_1.clear()

    def build_lexicon(self, input_filename, output_filename='out.txt', reset=True):
        """
        Builds the Lexicon by processing an input file, identifying neighbors, and saving results.

        Args:
            input_filename (str): The path to the input file containing words.
            output_filename (str): The path to the output file (default: 'out.txt').
            reset (bool): Whether to reset the Lexicon before building (default: True).
        """

        if reset: self.reset()

        # Generate AVL Tree
        print('Inserting data into AVL Tree...')
        self.read_data(input_filename)

        # Populate lists
        print('Populating lists...')
        self.word_tree.traverse_inorder(self.word_tree.root, self.sorted_list, self.same_char_0, self.same_char_1)

        # Add neighbours
        print('Adding neighbours...')
        self.add_all_neighbours()

        # Write to file
        print('Writing to file...')
        self.write_to_file(output_filename)

        print('Finished!\n')

    # NOTE: FUBAR ZONE START
    @staticmethod
    def compare_same_0(nested_list: list):
        counter: int = 0

        for same_len_list in nested_list:
            counter = 0

            while True:
                lists = Lexicon.yield_lists_same_0(same_len_list, counter)
                combined = []

                try:
                    for sublist in lists:
                        combined += sublist

                except TypeError:
                    break

                # TODO: Check if this works
                Lexicon.compare_words_same_list(combined)

                counter += 1

    @staticmethod
    def yield_lists_same_0(same_len_list: list, char_0_idx):

        # TODO: This takes a list of same_len words
        # It then digs 1 level into each sublist (of same_char_1 words)
        # It then yields a sublist at the specified yield_idx
        # Once no sublists remain, all are yielded

        out_of_range: int = 0

        for same_char_1 in same_len_list:
            try:
                yield same_char_1[char_0_idx]

            except IndexError:
                out_of_range += 1

        if out_of_range == len(same_len_list):
            yield None
