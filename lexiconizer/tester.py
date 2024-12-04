from lexicons.lexicon_quick import LexiconQuick
from lexicons.lexicon_radix import LexiconRadix
from lexicons.lexicon_dict import LexiconDict
from lexicons.lexicon_avl import LexiconAVL
from lexicons.lexicon_builtin import LexiconBuiltin
from lexicons.lexicon_benchmark import LexiconBenchmark
from utils.test_utils import compare_files, time_method

N_REPEATS = 20
args = [False, False, True]

AVL_CONST = 'avl.txt'
DICT_CONST = 'dict.txt'
QUICK_CONST = 'quick.txt'
RADIX_CONST = 'radix.txt'
BUILTIN_CONST = 'builtin.txt'
BENCHMARK_CONST = 'benchmark.txt'

# lexicon_dict = LexiconAVL()
# time_method(lexicon_dict.build_lexicon, 'in.txt', AVL_CONST, *args, verbose=True, n_repeats=N_REPEATS)

# lexicon_dict = LexiconDict()
# time_method(lexicon_dict.build_lexicon, 'in.txt', DICT_CONST, *args, verbose=True, n_repeats=N_REPEATS)

# lexicon_builtin = LexiconBuiltin()
# time_method(lexicon_builtin.build_lexicon, 'in.txt', BUILTIN_CONST, *args, verbose=True, n_repeats=N_REPEATS)

# lexicon_quick = LexiconQuick()
# time_method(lexicon_quick.build_lexicon, 'in.txt', QUICK_CONST, *args, verbose=True, n_repeats=N_REPEATS)

# lexicon_radix = LexiconRadix()
# time_method(lexicon_radix.build_lexicon, 'in.txt', RADIX_CONST, *args, verbose=True, n_repeats=N_REPEATS)

lexicon_benchmark = LexiconBenchmark()
time_method(lexicon_benchmark.build_lexicon, 'in.txt', BENCHMARK_CONST, *args, verbose=True, n_repeats=1)

compare_files([AVL_CONST, DICT_CONST, QUICK_CONST, RADIX_CONST, BUILTIN_CONST, BENCHMARK_CONST])

# # Results on windows
# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 5.21s across 20 runs
# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 3.02s across 20 runs
# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 3.05s across 20 runs
# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 3.23s across 20 runs
# All files match.

# # Results on linux
# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 2.69s across 20 runs
# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 1.39s across 20 runs
# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 1.40s across 20 runs
# Running build_lexicon 20 times...
# COMPLETE. Average execution time: 1.50s across 20 runs
# All files match.