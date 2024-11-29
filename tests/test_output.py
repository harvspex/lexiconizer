from dataclasses import dataclass, field
from filecmp import cmp

# TODO: Add docstrings
# TODO: Generally tidy up

@dataclass
class Word:
    spelling: str
    freq: int=1
    neighbours: list[str] = field(default_factory=list[str])

    def __str__(self):
        return f'{self.spelling} {self.freq} {self.neighbours}\n'

def is_neighbours(word, other_word):
    if len(word) != len(other_word):
        return False

    diffs = 0

    for i in range(len(word)):
        if word[i] != other_word[i]:
            diffs += 1

    return diffs == 1

lexicon = {}

with open('in.txt', 'r') as infile:
    for line in infile:
        tokens = line.lower().strip().split()

        for token in tokens:
            word = ''.join(_ for _ in token if _.isalpha())

            if word:
                try:
                    lexicon[word].freq += 1
                except:
                    lexicon[word] = Word(word)

lexicon = dict(sorted(lexicon.items()))

def generate(lexicon=lexicon):
    with open('out_test.txt', 'w') as outfile:
        keys = [k for k in lexicon.keys()]
        len_keys = len(keys)

        for a in range(len_keys):
            word_a = lexicon[keys[a]]

            for b in range(a+1, len_keys):
                word_b = lexicon[keys[b]]

                if is_neighbours(word_a.spelling, word_b.spelling):
                    word_a.neighbours.append(word_b.spelling)
                    word_b.neighbours.append(word_a.spelling)
            
            outfile.write(str(word_a))

def compare(
    test_filename: str='out.txt',
    control_filename:str='out_test.txt',
    shallow=False
):
    result = cmp(test_filename, control_filename, shallow=shallow)
    print(f'Files match: {result}')

def main():
    generate()
    compare()

if __name__ == '__main__':
    main()
