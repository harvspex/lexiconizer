#!/usr/bin/env python3

import argparse

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


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Lexiconizer: Count words and find neighbours'
    )

    # infile
    parser.add_argument('input_file', help='Input filename')

    # outfile
    parser.add_argument('output_file', help='Output filename')

    # gen control lexicon
    parser.add_argument(
        '-g', '--generate', '--gen',
        help='Generate a control lexicon',
        action='store_true'
    )

    # compare
    parser.add_argument(
        # TODO: Add option to specify control lexicon filename
        '-c', '--compare', '--comp --cmp',
        help='Compares lexicon against control lexicon',
        action='store_true'
    )

    # slow mode
    parser.add_argument(
        '-s', '--slow',
        help='Generates control lexicon even slower',
        action='store_true'
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

    return parser


def handle_lexicon(input_filename: str, output_filename: str, dict_mode: bool):
    from src.lexicon_avl import LexiconAVL
    from src.lexicon_dict import LexiconDict

    lexicon_type = LexiconDict if dict_mode else LexiconAVL

    lexicon = lexicon_type()
    lexicon.build_lexicon(input_filename, output_filename)


def handle_control_lexicon(input_filename: str, output_filename: str, slow_mode: bool):
    from tests.control_lexicon import ControlLexicon
    lexicon = ControlLexicon()
    lexicon.build_lexicon(input_filename, output_filename, slow_mode=slow_mode)


def handle_compare():
    pass


def handle_time():
    pass


def main():
    parser = get_parser()
    args = parser.parse_args()
    print(args)
    print(args.input_file)


if __name__ == '__main__':
    main()
