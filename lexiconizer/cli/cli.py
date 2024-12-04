import argparse
import cli.build_lexicons as build_lexicons
import cli.validation as validation
from cli.lexicon_type import LexiconType
from cli.lexicon_types_list import LEXICON_TYPES
from utils.test_utils import compare_files

# TODO: Improve help descriptions

def get_parser(lexicon_types: list[LexiconType]) -> argparse.ArgumentParser:
    DEFAULT_FILENAME: str = 'lexicon'

    parser = argparse.ArgumentParser(
        description='Lexiconizer: Count words and find neighbours'
    )
    # infile
    parser.add_argument(
        'input_file',
        help='filename or path of file to be lexiconized',
        type=validation.readable_file
    )
    # outfile
    parser.add_argument(
        '-o', '--output-file', '--output',
        help='specify the filename or path for output lexicon/s',
        default=DEFAULT_FILENAME,
        const=DEFAULT_FILENAME,
        type=validation.writeable_file,
        nargs='?'
    )
    # lexicons
    for l_type in lexicon_types:
        parser.add_argument(
            *l_type.flags,
            help=l_type.help,
            const=l_type.name,
            type=validation.writeable_file,
            nargs='?'
        )
    # time
    parser.add_argument(
        '-t', '--time',
        help='show runtime (optional: number of times to repeat lexicon generation, for more accurate average runtime)',
        const=1,
        type=validation.positive_int,
        nargs='?'
    )
    # verbose
    parser.add_argument(
        '-v', '--verbose',
        help='print the individual steps during lexicon generation (and its runtime if using `-t`)',
        action='store_true'
    )
    # compare
    parser.add_argument(
        '-c', '--compare', '--comp --cmp',
        help='compare all generated lexicons (optional: any number of other filenames for comparison)',
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

    # Match all LexiconType objects with corresponding arg in `args`.
    # Set LexiconType.filename to lexicon arg value.
    for l_type in lexicon_types:
        l_type.filename = getattr(args, l_type.name)

    # Build all lexicons
    return build_lexicons.build_all_lexicons(
        input_file=args.input_file,
        output_file=args.output_file,
        time=args.time,
        verbose=args.verbose,
        lexicon_types=lexicon_types
    )


def handle_compare(args: argparse.Namespace, filenames: list[str]):
    if args.compare is not None:
        compare_files(filenames + args.compare)


def main():
    parser = get_parser(LEXICON_TYPES)
    args = parser.parse_args()
    handle_args(args, LEXICON_TYPES)
