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
from cli.lexicon_types import get_lexicon_types

# TODO: Improve help descriptions

def get_parser(lexicon_types: list[LexiconType]) -> argparse.ArgumentParser:
    LEXICON_CONST: str = 'lexicon'
    LEXICON_TYPE_CONST: str = ''

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
    for l_type in lexicon_types:
        parser.add_argument(
            *l_type.flags,
            help=l_type.help,
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


def handle_args(args: argparse.Namespace, lexicon_types: list[LexiconType]):
    filenames: list[str] = handle_build_all_lexicons(args, lexicon_types)
    handle_compare(args, filenames)


def handle_build_all_lexicons(
    args: argparse.Namespace,
    lexicon_types: list[LexiconType]
) -> list[str]:

    # Match all lexicon args with corresponding LexiconType object.
    # Set LexiconType.filename to lexicon arg value.
    for l_type in lexicon_types:
        l_type.filename = getattr(args, l_type.name)

    # Build all lexicons
    return cli_helpers.build_all_lexicons(
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
    lexicon_types = get_lexicon_types()
    parser = get_parser(lexicon_types)
    args = parser.parse_args()
    handle_args(args, lexicon_types)
