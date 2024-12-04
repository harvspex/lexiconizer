from cli.lexicon_type import LexiconType
from lexicons.lexicon_avl import LexiconAVL
from lexicons.lexicon_dict import LexiconDict
from lexicons.lexicon_benchmark import LexiconBenchmark
from sorting.quick_sort import quick_sort
from sorting.radix_sort import radix_sort
"""
Contains the `LEXICON_TYPES` list, which facilitates adding new lexicon types.

`LEXICON_TYPES` contains a list of LexiconType objects, which contain 
all data needed to build the corresponding lexicon type, AND add new 
flags to the argparse parser. When a new lexicon type is created, simply
adding it to this list will seamlessly integrate it into Lexiconizer.

Note that the order of the list is the order in which:
    - Lexicons are executed, if more than one are specified
    - Lexicon flags are printed (when -h is used)
"""

LEXICON_TYPES = [
    LexiconType(
        lexicon_type=LexiconDict,
        flags=['-d', '--default'],
        help='Generates lexicon using dictionary. Sorts with built-in method `sorted`'
    ),
    LexiconType(
        lexicon_type=LexiconDict,
        flags=['-q', '--quicksort', '--quick'],
        help='Generates lexicon using dictionary. Sorts with quick sort',
        sorting_method=quick_sort
    ),
    LexiconType(
        lexicon_type=LexiconDict,
        flags=['-r', '--radix-sort', '--radix'],
        help='Generates lexicon using dictionary. Sorts with radix sort',
        sorting_method=radix_sort
    ),
    LexiconType(
        lexicon_type=LexiconAVL,
        flags=['-a', '--avl-tree', '--avl'],
        help='Generates lexicon using AVL Tree. Sorts with in-order traversal'
    ),
    LexiconType(
        lexicon_type=LexiconBenchmark,
        flags=['-b', '--benchmark'],
        help='Generate a benchmark lexicon. Uses minimal optimisations for adding neighbours'
    )
]
