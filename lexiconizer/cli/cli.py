import argparse
from dataclasses import dataclass

import cli.cli_helpers as cli_helpers
import cli.validation as validation
from cli.lexicon_type import LexiconType
from lexicons.lexicon_avl import LexiconAVL
from lexicons.lexicon_dict import LexiconDict
from lexicons.lexicon_benchmark import LexiconBenchmark
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


def handle_args(args: argparse.Namespace):
    filenames: list[str] = handle_build_all_lexicons(args)
    handle_compare(args, filenames)


def handle_build_all_lexicons(args: argparse.Namespace):

    lexicon_types = [
        LexiconType(LexiconAVL, args.avl_tree, '_avl'),
        LexiconType(LexiconDict, args.dictionary, '_dict'),
        LexiconType(LexiconDict, args.quick_sort, '_quick', quick_sort),
        LexiconType(LexiconDict, args.radix_sort, '_radix', radix_sort),
        LexiconType(LexiconBenchmark, args.benchmark, '_benchmark')
    ]
    cli_helpers.build_all_lexicons(
        input_file=args.input_file,
        output_file=args.output_file,
        time=args.time,
        verbose=args.verbose,
        lexicon_types=lexicon_types
    )

def handle_compare(args: argparse.Namespace, filenames: list[str]):
    if args.compare:
        cli_helpers.compare_files(filenames)

def main():
    parser = get_parser()
    args = parser.parse_args()

    print(getattr(args, 'input_file'))
    quit()

    handle_args(args)
