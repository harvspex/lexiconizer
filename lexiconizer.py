#!/usr/bin/env python3

import argparse
from src.lexicon_avl import LexiconAVL
from src.lexicon_dict import LexiconDict
from src.lexicon_benchmark import LexiconBenchmark
from utils.test_utils import time_method


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
    # gen benchmark lexicon
    parser.add_argument(
        # TODO: Add option to specify benchmark lexicon filename
        '-b', '--benchmark',
        help='Generate a benchmark lexicon',
        action='store_true'
    )
    # parser.add_argument(
    #     'benchmark_file',
    #     nargs='?',
    #     help='Optional filename for benchmark lexicon'
    # )
    # slow mode
    parser.add_argument(
        '-s', '--slow',
        help='Generates benchmark lexicon even slower',
        action='store_true'
    )
    # compare
    parser.add_argument(
        # TODO: Add option to specify benchmark lexicon filename
        '-c', '--compare', '--comp --cmp',
        help='Compares lexicon against benchmark lexicon',
        action='store_true'
    )

    return parser


def handle_args(args: argparse.Namespace):
    # TODO: Ugly, fix
    if args.time and not args.verbose:
        lexicon_args = [args.input_file, args.output_file, args.verbose]
    else:
        lexicon_args = [args.input_file, args.output_file, args.time, args.verbose]

    # TODO: This can now be improved, because LexiconBenchmark can be treated as a Lexicon

    # Generate benchmark lexicon
    if args.benchmark:
        lexicon_benchmark = LexiconBenchmark(slow_mode=args.slow)
        lexicon_benchmark.build_lexicon(*lexicon_args)

    # Build lexicon
    lexicon_type = LexiconDict if args.dictionary else LexiconAVL
    lexicon = lexicon_type()

    if args.time:
        time_method(lexicon.build_lexicon, *lexicon_args) # TODO: add N repeats from args.time
    else:
        lexicon.build_lexicon(*lexicon_args)

    if args.compare:
        pass

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
    args = parser.parse_args()
    handle_args(args)

    # # Might be a way to individually parse -c, -g (etc.) first

    # args = parser.parse_args(['input_file', 'output_file'])
    # print(args)

    # args = parser.parse_args()
    # print(args)



if __name__ == '__main__':
    main()
