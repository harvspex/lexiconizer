from lexicons.lexicon_quick import LexiconQuick
from lexicons.lexicon_radix import LexiconRadix
from lexicons.lexicon_dict import LexiconDict
from lexicons.lexicon_avl import LexiconAVL
from utils.test_utils import compare_files, time_method

N_REPEATS = 20
args = [False, False, True]

AVL_CONST = 'avl.txt'
lexicon_dict = LexiconAVL()
time_method(lexicon_dict.build_lexicon, 'in.txt', AVL_CONST, *args, verbose=True, n_repeats=N_REPEATS)

DICT_CONST = 'dict.txt'
lexicon_dict = LexiconDict()
time_method(lexicon_dict.build_lexicon, 'in.txt', DICT_CONST, *args, verbose=True, n_repeats=N_REPEATS)

QUICK_CONST = 'quick.txt'
lexicon_quick = LexiconQuick()
time_method(lexicon_quick.build_lexicon, 'in.txt', QUICK_CONST, *args, verbose=True, n_repeats=N_REPEATS)

RADIX_CONST = 'radix.txt'
lexicon_radix = LexiconRadix()
time_method(lexicon_radix.build_lexicon, 'in.txt', RADIX_CONST, *args, verbose=True, n_repeats=N_REPEATS)

compare_files([AVL_CONST, DICT_CONST, QUICK_CONST, RADIX_CONST])

# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 5.21s across 20 runs
# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 3.02s across 20 runs
# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 3.05s across 20 runs
# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 3.23s across 20 runs
# All files match.
