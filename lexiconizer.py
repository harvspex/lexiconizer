#!/usr/bin/env python3

import argparse
from src.lexicon_avl import LexiconAVL
from src.lexicon_dict import LexiconDict
from tests.control_lexicon import ControlLexicon


def get_parser() -> argparse.ArgumentParser:
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
        'output_file',
        help='Output filename'
    )
    # dict mode
    parser.add_argument(
        '-d', '--dictionary', '--dict',
        help='Generates lexicon using dict',
        action='store_true'
    )
    # time
    parser.add_argument(
        # TODO: Take an int as num of repeats
        '-t', '--time',
        help='Shows runtime',
        action='store_true'
    )
    # verbose
    parser.add_argument(
        '-v', '--verbose',
        help='Increases the amount of printed text',
        action='store_true'
    )
    # gen control lexicon
    parser.add_argument(
        # TODO: Add option to specify control lexicon filename
        '-g', '--generate', '--gen',
        help='Generate a control lexicon',
        action='store_true'
    )
    # parser.add_argument(
    #     'control_file',
    #     nargs='?',
    #     help='Optional filename for control lexicon'
    # )
    # slow mode
    parser.add_argument(
        '-s', '--slow',
        help='Generates control lexicon even slower',
        action='store_true'
    )
    # compare
    parser.add_argument(
        # TODO: Add option to specify control lexicon filename
        '-c', '--compare', '--comp --cmp',
        help='Compares lexicon against control lexicon',
        action='store_true'
    )

    return parser


def handle_args(args: argparse.Namespace):
    lexicon_args = [args.input_file, args.output_file, args.time, args.verbose]

    print(args.control_file)

    # Generate control lexicon
    if args.generate:
        control_lexicon = ControlLexicon()
        control_lexicon_args = lexicon_args.append(args.slow)
        control_lexicon.build_lexicon(*control_lexicon_args)

    # Build lexicon
    lexicon_type = LexiconDict if args.dictionary else LexiconAVL
    lexicon = lexicon_type()
    lexicon.build_lexicon(*lexicon_args)

    if args.compare:
        pass


# TODO: Delete
def handle_control_lexicon(input_filename: str, output_filename: str, slow_mode: bool):
    from tests.control_lexicon import ControlLexicon
    lexicon = ControlLexicon()
    lexicon.build_lexicon(input_filename, output_filename, slow_mode=slow_mode)


# Example use:
#
# lexiconizer in.txt out.txt -g out_control.txt -s -c -t 10 -v -d
#
# This should:
#   - Read in.txt
#   - Build a LexiconDict in verbose mode
#   - Write to out.txt
#   - Repeat the above 10 times, timing each method
#
# Then:
#   - Build a control dict with slow, verbose, and timed modes (only once)
#   - Write control dict to out_control.txt
#   - compare out.txt to out_control.txt

def main():
    parser = get_parser()

    # Might be a way to individually parse -c, -g (etc.) first

    args = parser.parse_args(['input_file', 'output_file'])
    print(args)

    args = parser.parse_args()
    print(args)

    quit()
    return

    # args = parser.parse_args()
    # handle_args(args)


if __name__ == '__main__':
    main()
