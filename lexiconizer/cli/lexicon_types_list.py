from lexiconizer.cli.lexicon_type import LexiconType
from lexiconizer.lexicons.lexicon_avl import LexiconAVL
from lexiconizer.lexicons.lexicon_dict import LexiconDict
from lexiconizer.lexicons.lexicon_benchmark import LexiconBenchmark
from lexiconizer.lexicons.lexicon_radix import LexiconRadix
from lexiconizer.sorting.quick_sort import quick_sort
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

def get_help(sorting_method: str=None):
    """
    Make a default help message.

    Args:
        sorting_method (str, optional): the sorting method or data 
            structure used to generate this type of lexicon.
            (default=None)

    Returns:
        help_message (str): A string containing a help message. If
            `sorting_method` is None, just returns the default message.
    """
    help_message: str = '(optional: filename or path for this lexicon)'

    if sorting_method:
        help_message = f'generate lexicon using {sorting_method} {help_message}'

    return help_message

LEXICON_TYPES = [
    LexiconType(
        lexicon_type=LexiconDict,
        flags=['-d', '--default'],
        help=get_help('built-in `sorted` method')
    ),
    LexiconType(
        lexicon_type=LexiconDict,
        flags=['-q', '--quicksort', '--quick'],
        help=get_help('quicksort'),
        sorting_method=quick_sort
    ),
    LexiconType(
        lexicon_type=LexiconRadix,
        flags=['-r', '--radix-sort', '--radix'],
        help=get_help('radix sort'),
    ),
    LexiconType(
        lexicon_type=LexiconAVL,
        flags=['-a', '--avl-tree', '--avl'],
        help=get_help('AVL tree')
    ),
    LexiconType(
        lexicon_type=LexiconBenchmark,
        flags=['-b', '--benchmark'],
        help='generate a "benchmark" lexicon (has minimal optimisations for adding neighbours) '+get_help()
    )
]
