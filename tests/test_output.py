import filecmp
import utils.neighbours_utils as neighbours_utils
from src.word import Word
"""
Contains methods to generate and compare a control lexicon against the one created by Lexiconizer.

NOTE: Generating a control lexicon for large files is pretty slow!
"""
# NOTE: This has also been made somewhat redundant, due to `LexiconDict` 
# TODO: Fix error. Currently run with: python3 -m tests.test_output
# TODO: Add docstrings
def read_data(lexicon: dict[str,Word]={}, input_filename='in.txt') -> dict[str,Word]:
    print('Reading and inserting data...')
    with open(input_filename, 'r') as infile:
        for line in infile:
            tokens = line.lower().strip().split()

            for token in tokens:
                word = ''.join(_ for _ in token if _.isalpha())

                if word:
                    try:
                        lexicon[word].frequency += 1
                    except:
                        lexicon[word] = Word(word)

    return dict(sorted(lexicon.items()))

def chars_match(spelling_a: str, spelling_b: str, index: int):
    return spelling_a[index] == spelling_b[index]

def is_neighbours_candidate(spelling_a: str, spelling_b: str) -> bool:
    if len(spelling_a) != len(spelling_b):
        return False

    elif len(spelling_a) == 1:
        return True

    return (
        chars_match(spelling_a, spelling_b, index=0)
        or chars_match(spelling_a, spelling_b, index=1)
    )

def generate(lexicon: dict[str,Word], output_filename='lexicon_test.txt'):
    print('Adding neighbours and writing to file (SLOW)...')
    with open(output_filename, 'w') as outfile:
        keys = [k for k in lexicon.keys()]
        len_keys = len(keys)

        for a in range(len_keys):
            spelling_a = keys[a]
            word_a = lexicon[spelling_a]

            for b in range(a+1, len_keys):
                spelling_b = keys[b]
                word_b = lexicon[spelling_b]

                if not is_neighbours_candidate(spelling_a, spelling_b):
                    continue

                elif neighbours_utils.word_is_neighbours(word_a, word_b):
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
    lexicon: dict[str,Word] = read_data()
    generate(lexicon)
    compare()

if __name__ == '__main__':
    main()
