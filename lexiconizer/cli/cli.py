import argparse
import lexiconizer.cli.build_lexicons as build_lexicons
import lexiconizer.cli.validation as validation
from lexiconizer.cli.lexicon_type import LexiconType
from lexiconizer.cli.lexicon_types_list import LEXICON_TYPES
from lexiconizer.utils.test_utils import compare_files

def get_parser(lexicon_types: list[LexiconType]) -> argparse.ArgumentParser:
    """
    Creates an argument parser for the lexiconizer CLI.

    Args:
        lexicon_types (list[LexiconType]): A list of LexiconType 
            objects, each representing a type of lexicon to be generated

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    DEFAULT_FILENAME: str = 'lexicon'

    parser = argparse.ArgumentParser(
        description='lexiconizer: count words and find neighbours'
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
    """
    Handles the parsed arguments by building lexicons and optionally comparing them.

    Args:
        args (argparse.Namespace): The parsed CLI arguments.
        lexicon_types (list[LexiconType]): A list of LexiconType objects
            representing the lexicons to be built.
    """
    # Build all lexicons and get filenames
    filenames: list[str] = handle_build_all_lexicons(args, lexicon_types)

    # Compare filenames (if applicable)
    handle_compare(args, filenames)


def handle_build_all_lexicons(
    args: argparse.Namespace,
    lexicon_types: list[LexiconType]
) -> list[str]:
    """
    Builds all specified lexicons based on CLI arguments.

    Args:
        args (argparse.Namespace): The parsed CLI arguments.
        lexicon_types (list[LexiconType]): A list of LexiconType objects
            representing the lexicons to be built.

    Returns:
        list[str]: A list of filenames for the generated lexicons.
    """
    # Set each LexiconType.filename to corresponding lexicon arg value
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
    """
    Compares generated lexicons with additional files, if specified.

    Args:
        args (argparse.Namespace): The parsed CLI arguments.
        filenames (list[str]): A list of filenames for the generated lexicons.
    """
    if args.compare is not None:
        compare_files(filenames + args.compare)


def main():
    """
    Entry point for the lexiconizer CLI application. Parses arguments,
    handles lexicon generation, and performs comparisons if requested.
    """
    parser = get_parser(LEXICON_TYPES)
    args = parser.parse_args()
    handle_args(args, LEXICON_TYPES)
