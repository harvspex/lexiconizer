import filecmp
from dataclasses import dataclass, field
import utils.neighbours_utils as neighbours_utils
from src.word_tree import Word
"""
Contains methods to generate and compare a control lexicon against the one created by Lexiconizer.

NOTE: Generating a control lexicon for large files is pretty slow!
"""
# TODO: Fix error
# TODO: Add docstrings
def read_data(lexicon: dict[str,Word], input_filename='in.txt') -> dict[str,Word]:
    with open(input_filename, 'r') as infile:
        for line in infile:
            tokens = line.lower().strip().split()

            for token in tokens:
                word = ''.join(_ for _ in token if _.isalpha())

                if word:
                    try:
                        lexicon[word].freq += 1
                    except:
                        lexicon[word] = Word(word)

    return dict(sorted(lexicon.items()))

def generate(lexicon: dict[str,Word], output_filename='lexicon_test.txt'):
    with open(output_filename, 'w') as outfile:
        keys = [k for k in lexicon.keys()]
        len_keys = len(keys)

        for a in range(len_keys):
            word_a = lexicon[keys[a]]

            for b in range(a+1, len_keys):
                word_b = lexicon[keys[b]]

                if neighbours_utils.word_is_neighbours(word_a, word_b):
                    neighbours_utils.add_mutual_neighbours(word_a, word_b)
            
            outfile.write(str(word_a))

def compare(
    test_filename: str='lexicon.txt',
    control_filename:str='lexicon_test.txt',
    shallow=False
) -> bool:
    result = filecmp.cmp(test_filename, control_filename, shallow=shallow)
    print(f'Files match: {result}')
    return result

def main():
    generate()
    compare()

if __name__ == '__main__':
    main()
