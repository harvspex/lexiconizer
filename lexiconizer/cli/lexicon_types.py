from cli.lexicon_type import LexiconType
from lexicons.lexicon_avl import LexiconAVL
from lexicons.lexicon_dict import LexiconDict
from lexicons.lexicon_benchmark import LexiconBenchmark
from sorting.quick_sort import quick_sort
from sorting.radix_sort import radix_sort

def get_lexicon_types():
    LEXICON_TYPES = [
        LexiconType(
            lexicon_type=LexiconDict,
            flags=['-d', '--default'],
            help='Generates lexicon using dictionary. Sorts with built-in method `sorted`'
        ),
        LexiconType(
            lexicon_type=LexiconDict,
            flags=['-q', '--quick-sort', '--quick'],
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
    return LEXICON_TYPES