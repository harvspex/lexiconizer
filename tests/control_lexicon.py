# TODO: Docstrings?

class ControlWord:
    def __init__(self, spelling):
        self.spelling: str = spelling
        self.neighbours: list[str] = []
        self.frequency: int = 1
        self.pointer: int = 0

    def __str__(self) -> str:
        return f"{self.spelling} {self.frequency} {self.neighbours}\n"

class ControlLexicon:
    def __init__(self):
        self.lexicon: dict[str, ControlWord] = {}

    def build_lexicon (
        self, input_filename: str,
        output_filename: str,
        reset: bool=True,
        slow_mode: bool=False
    ):
        if reset: self.lexicon.clear()

        print('Reading and inserting data...')
        self.read_data(input_filename)

        print('Sorting lexicon...')
        self.lexicon = dict(sorted(self.lexicon.items()))

        print('Adding neighbours...')
        self.add_all_neighbours(slow_mode=slow_mode)

        print('Writing to file...')
        self.write_to_file(output_filename)

        print('Finished!\n')

    def read_data(self, input_filename: str):
        with open(input_filename, 'r') as infile:
            for line in infile:
                tokens = line.lower().strip().split()

                for token in tokens:
                    word = ''.join(_ for _ in token if _.isalpha())

                    if word:
                        try:
                            self.lexicon[word].frequency += 1
                        except:
                            self.lexicon[word] = ControlWord(word)

    def write_to_file(self, filename: str):
        with open(filename, 'w') as outfile:
            for i in self.lexicon.values():
                outfile.write(str(i))

    @staticmethod
    def chars_match(spelling_a: str, spelling_b: str, index: int):
        return spelling_a[index] == spelling_b[index]

    @staticmethod
    def is_neighbours_candidate(spelling_a: str, spelling_b: str) -> bool:
        if len(spelling_a) != len(spelling_b):
            return False

        elif len(spelling_a) == 1:
            return True

        return (
            ControlLexicon.chars_match(spelling_a, spelling_b, index=0)
            or ControlLexicon.chars_match(spelling_a, spelling_b, index=1)
        )

    @staticmethod
    def word_is_neighbours(word_a: ControlWord, word_b: ControlWord) -> bool:
        spelling_a = word_a.spelling
        spelling_b = word_b.spelling

        if len(spelling_a) != len(spelling_b):
            return False

        diffs = 0

        for i in range(len(spelling_a)):

            if spelling_a[i] != spelling_b[i]:
                diffs += 1

                if diffs > 1:
                    return False

        return True

    @staticmethod
    def add_mutual_neighbours(word_a: ControlWord, word_b: ControlWord):
        word_a.neighbours.append(word_b.spelling)
        word_b.neighbours.append(word_a.spelling)

    def add_all_neighbours(self, slow_mode:int=False):
        if slow_mode: self.add_all_neighbours_slow()
        else: self.add_all_neighbours_fast()

    def add_all_neighbours_fast(self):
        keys = list(self.lexicon.keys())
        len_keys = len(keys)

        for a in range(len_keys):
            spelling_a = keys[a]
            word_a = self.lexicon[spelling_a]

            for b in range(a+1, len_keys):
                spelling_b = keys[b]
                word_b = self.lexicon[spelling_b]

                if (self.is_neighbours_candidate(spelling_a, spelling_b)
                    and ControlLexicon.word_is_neighbours(word_a, word_b)):

                        ControlLexicon.add_mutual_neighbours(word_a, word_b)

    def add_all_neighbours_slow(self):
        word_list: list[ControlWord] = list(self.lexicon.values())
        for word_a in word_list:
            for word_b in word_list:
                if ControlLexicon.word_is_neighbours(word_a, word_b):
                    word_a.neighbours.append(word_b.spelling)
