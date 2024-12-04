import argparse
# from collections import namedtuple
from dataclasses import dataclass, field
from typing import Callable

import cli.validation as validation
from lexicons.lexicon import Lexicon
from lexicons.lexicon_avl import LexiconAVL
from lexicons.lexicon_dict import LexiconDict
from lexicons.lexicon_benchmark import LexiconBenchmark
from utils.test_utils import time_method, compare_files
from sorting.quick_sort import quick_sort
from sorting.radix_sort import radix_sort

# TODO: Improve help descriptions

def get_parser() -> argparse.ArgumentParser:
    LEXICON_CONST: str = 'lexicon'
    LEXICON_TYPE_CONST: str = ''

    @dataclass
    class LexiconFlag:
        flags: list[str]
        help: str

    lexicon_flags = [
        LexiconFlag(['-a', '--avl-tree', '--avl'],
        help='Generates lexicon using AVL Tree'),

        LexiconFlag(['-d', '--dictionary', '--dict'],
        help='Generates lexicon using dict'),

        LexiconFlag(['-q', '--quick-sort', '--quick'],
        help='Generates lexicon using dictionary. Sorts with quick sort'),

        LexiconFlag(['-r', '--radix-sort', '--radix'],
        help='Generates lexicon using dictionary. Sorts with radix sort'),

        LexiconFlag(['-b', '--benchmark'],
        help='Generate a benchmark lexicon')
    ]

    parser = argparse.ArgumentParser(
        description='Lexiconizer: Count words and find neighbours'
    )
    # infile
    parser.add_argument(
        'input_file',
        help='Input filename',
        type=validation.readable_file
    )
    # outfile
    parser.add_argument(
        '-o', '--output-file', '--output',
        help='Output filename',
        default=LEXICON_CONST,
        const=LEXICON_CONST,
        type=validation.writeable_file,
        nargs='?'
    )
    # lexicons
    for flag in lexicon_flags:
        parser.add_argument(
            *flag.flags,
            help=flag.help,
            const=LEXICON_TYPE_CONST,
            type=validation.writeable_file,
            nargs='?'
        )
    # time
    parser.add_argument(
        '-t', '--time',
        help='Shows runtime',
        const=1,
        type=validation.positive_int,
        nargs='?'
    )
    # verbose
    parser.add_argument(
        '-v', '--verbose',
        help='Increases the amount of printed text',
        action='store_true'
    )
    # compare
    parser.add_argument(
        '-c', '--compare', '--comp --cmp',
        help='Compares lexicon against benchmark lexicon',
        type=validation.readable_file,
        nargs='*'
    )

    return parser


def handle_args(args: argparse.Namespace) -> list[str]:
    @dataclass
    class LexiconType:
        type: type
        filename: validation.writeable_file
        default_name: str
        sorting_method: Callable=None

    lexicon_types = [
        LexiconType(LexiconAVL, args.avl_tree, '_avl'),
        LexiconType(LexiconDict, args.dictionary, '_dict'),
        LexiconType(LexiconDict, args.quick_sort, '_quick', quick_sort),
        LexiconType(LexiconDict, args.radix_sort, '_radix', radix_sort),
        LexiconType(LexiconBenchmark, args.benchmark, '_benchmark')
    ]

    none_counter: int = 0
    filenames: list[str] = []

    for lexicon_type in lexicon_types:
        match lexicon_type.filename:
            case None:
                none_counter += 1
                continue
            case '':
                filename = args.output_file + lexicon_type.default_name
            case _:
                filename = lexicon_type.filename

        build_lexicon(lexicon_type.type, filename, args, lexicon_type.sorting_method)
        filenames.append(filename)

    # TODO: Could be nicer
    if len(lexicon_types) == none_counter:
        build_lexicon(LexiconAVL, args.output_file, args)
        filenames.append(args.output_file)

    if args.compare is not None:
        compare_files(filenames + args.compare)


def build_lexicon(
    lexicon_type: type,
    output_file: str,
    args: argparse.Namespace,
    sorting_method: Callable=None
):
    # TODO: If verbose, print lexicon type (not running build_lexicon)

    #  -t and -v interaction:
    #   t + v = just time individual step
    #   t     = just time entire routine
    #   v     = just print individual steps
    #   _     = totally slient

    # n_repeats is always 1 for LexiconBenchmark

    lexicon: Lexicon

    if sorting_method is not None:
        lexicon = lexicon_type(sorting_method)
    else:
        lexicon = lexicon_type()

    time: bool = args.time is not None
    time_lexicon: bool = False if (time and not args.verbose) else time
    build_lexicon_args = [args.input_file, output_file, args.verbose, time_lexicon]

    if not time:
        lexicon.build_lexicon(*build_lexicon_args)
        return

    n_repeats: int = args.time
    print_average: bool = True if (n_repeats > 1) else False

    if lexicon_type is LexiconBenchmark:
        n_repeats = 1

    time_method(
        lexicon.build_lexicon,
        *build_lexicon_args,
        n_repeats=n_repeats,
        verbose=print_average
    )


def main():
    parser = get_parser()
    args = parser.parse_args()
    handle_args(args)
