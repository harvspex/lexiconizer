from src.lexicon_dict import LexiconDict

from tests.test_output import compare

input_filename: str = 'in.txt'
output_filename: str = 'lexicon.txt'
repeats: int = 1
lexicon: LexiconDict = LexiconDict()
lexicon.build_lexicon(input_filename, output_filename)
compare()