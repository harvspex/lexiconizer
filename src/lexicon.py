from src.word_tree import Word
import utils.one_char_utils as one_char_utils
import utils.same_char_0_utils as same_char_0_utils
import utils.same_char_1_utils as same_char_1_utils

# NOTE: staticmethods may be slower. Do testing.
# TODO: init with filename, and run build_lexicon on init?
# TODO: Could add option to time build_lexicon subtasks individually
# TODO: Handle IOError if files cannot be read

# TODO: Change to superclass for lexicon_dict and lexicon_avl

class Lexicon:
    def __init__(self):
        self.one_char_words: list[Word] = []
        self.nested_word_lists: list = []

    def read_data(self, filename: str): pass

    def write_to_file(self, filename: str):
        """
        Writes the sorted list of words to a file.

        Args:
            filename (str): The path to the output file where data will be written.

        Raises:
            IOError: If the file cannot be written.
        """
        with open(filename, 'w') as outfile:
            for i in self.sorted_list:
                outfile.write(str(i))

    def add_all_neighbours(self):
        """
        Executes all neighbor-finding methods, including:
            `one_char_utils.add_neighbours`
            `same_char_0_utils.add_neighbours`
            `same_char_1_utils.add_neighbours`
        """
        one_char_utils.add_neighbours(self.one_char_words)
        same_char_0_utils.add_neighbours(self.nested_word_lists)
        same_char_1_utils.add_neighbours(self.nested_word_lists)

    def reset(self):
        """Resets the lexicon."""
        self.one_char_words.clear()
        self.nested_word_lists.clear()

    def build_lexicon(self, input_filename: str, output_filename: str):

        # Add neighbours
        print('Adding neighbours...')
        self.add_all_neighbours()

        # Write to file
        print('Writing to file...')
        self.write_to_file(output_filename)

        print('Finished!\n')
