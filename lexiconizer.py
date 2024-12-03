#!/usr/bin/env python3

import argparse
from collections import namedtuple
from src.lexicon.lexicon import Lexicon
from src.lexicon.lexicon_avl import LexiconAVL
from src.lexicon.lexicon_dict import LexiconDict
from src.lexicon.lexicon_benchmark import LexiconBenchmark
from src.utils.test_utils import time_method, compare_files

# TODO: Move to /src
# TODO: Move cli/argparse stuff to cli.py
# TODO: Improve help descriptions

def get_parser() -> argparse.ArgumentParser:
    LEXICON_CONST: str = 'lexicon'
    LEXICON_TYPE_CONST: str = ''

    parser = argparse.ArgumentParser(
        description='Lexiconizer: Count words and find neighbours'
    )
    # infile
    parser.add_argument(
        'input_file',
        help='Input filename'
    )
    # outfile
    parser.add_argument(
        '-o', '--output-file', '--output',
        help='Output filename',
        default=LEXICON_CONST,
        const=LEXICON_CONST,
        type=str,
        nargs='?'
    )
    # lexicon avl
    parser.add_argument(
        '-a', '--avl-tree', '--avl',
        help='Generates lexicon using AVL Tree',
        const=LEXICON_TYPE_CONST,
        type=str,
        nargs='?'
    )
    # lexicon dict
    parser.add_argument(
        '-d', '--dictionary', '--dict-test',
        help='Generates lexicon using dict',
        const=LEXICON_TYPE_CONST,
        type=str,
        nargs='?'
    )
    # lexicon benchmark
    parser.add_argument(
        # TODO: Add option to specify benchmark lexicon filename
        '-b', '--benchmark',
        help='Generate a benchmark lexicon',
        const=LEXICON_TYPE_CONST,
        type=str,
        nargs='?'
    )
    # time
    parser.add_argument(
        # TODO: Take an int as num of repeats
        '-t', '--time',
        help='Shows runtime',
        const=1,
        type=positive_int,
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
        type=str,
        nargs='*'
    )

    return parser


def positive_int(value):
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(
                f'Invalid value: {value}. Must be an integer greater than 0.'
            )
        return ivalue

    except ValueError:
        raise argparse.ArgumentTypeError(
            f'Invalid value: {value}. Must be an integer.'
        )


def build_lexicon(lexicon_type: type, output_file: str, args: argparse.Namespace):
    # TODO: If verbose, print lexicon type (not running build_lexicon)

    #  -t and -v interaction:
    #   t + v = just time individual step
    #   t     = just time entire routine
    #   v     = just print individual steps
    #   _     = totally slient

    # n_repeats is always 1 for LexiconBenchmark

    lexicon: Lexicon = lexicon_type()
    time: bool = (args.time is not None) # and (args.time > 0)
    time_lexicon: bool = False if (time and not args.verbose) else time
    lexicon_args = [args.input_file, output_file, args.verbose, time_lexicon]

    if args.time is None:
        lexicon.build_lexicon(*lexicon_args)
        return

    n_repeats: int = args.time
    print_average: bool = True if (n_repeats > 1) else False

    if lexicon_type is LexiconBenchmark:
        n_repeats = 1

    time_method(
        lexicon.build_lexicon,
        *lexicon_args,
        n_repeats=n_repeats,
        verbose=print_average
    )


def handle_args(args: argparse.Namespace) -> list[str]:

    LexiconTuple = namedtuple('LexiconTuple', ['type', 'filename', 'default'])

    lexicon_types = [
        LexiconTuple(LexiconAVL, args.avl_tree, '_avl'),
        LexiconTuple(LexiconDict, args.dictionary, '_dict'),
        LexiconTuple(LexiconBenchmark, args.benchmark, '_benchmark')
    ]

    none_counter: int = 0
    filenames: list[str] = []

    for lexicon_type in lexicon_types:
        match lexicon_type.filename:
            case None:
                none_counter += 1
                continue
            case '':
                filename = args.output_file + lexicon_type.default
            case _:
                filename = lexicon_type.filename

        build_lexicon(lexicon_type.type, filename, args)
        filenames.append(filename)

    # TODO: Could be nicer
    if len(lexicon_types) == none_counter:
        build_lexicon(LexiconAVL, args.output_file, args)
        filenames.append(args.output_file)

    if args.compare is not None:
        compare_files(filenames + args.compare)


def main():
    parser = get_parser()
    args = parser.parse_args()
    handle_args(args)


if __name__ == '__main__':
    main()
