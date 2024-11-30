# TODO: Should be a subclass of lexicon, using a dict.
# This is to compare the speed of the avl version against a builtin version.

from src.lexicon import Lexicon, Word

# NOTE: staticmethods may be slower. Do testing.
# TODO: init with filename, and run build_lexicon on init?
# TODO: Could add option to time build_lexicon subtasks individually
# TODO: Handle IOError if files cannot be read

class LexiconDict(Lexicon):
    def __init__(self):
        self.dictionary: dict[str, Word] = {}

    def read_data(self, filename: str):
        with open(filename, 'r') as infile:
            for line in infile:
                tokens = line.lower().strip().split()

                for token in tokens:
                    data = ''.join(c for c in token if c.isalpha())

                    if data:
                        self.dictionary.insert_element(data)

    def reset(self):
        """Resets the lexicon."""
        self.dictionary.clear()
        self.sorted_list.clear()
        self.one_char_words.clear()
        self.nested_word_lists.clear()

    def build_lexicon(self, input_filename: str, output_filename: str, reset: bool=True):
        """
        Builds the Lexicon. Processes input, adds neighbors, and saves results.

        Args:
            input_filename (str): The path to the input file containing words.
            output_filename (str): The path to the output file.
            reset (bool): Whether to reset the Lexicon before building
                (default: True).
        """

        if reset: self.reset()

        # Generate AVL Tree
        print('Inserting data into AVL Tree...')
        self.read_data(input_filename)

        # Populate lists
        print('Populating lists...')
        self.dictionary.traverse_inorder(
            self.dictionary.root,
            self.sorted_list,
            self.one_char_words,
            self.nested_word_lists
        )

        # Add neighbours
        print('Adding neighbours...')
        self.add_all_neighbours()

        # Write to file
        print('Writing to file...')
        self.write_to_file(output_filename)

        print('Finished!\n')
