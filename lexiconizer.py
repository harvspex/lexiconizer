#!/usr/bin/env python3

# TODO: Move to /src
# TODO: Change name to cli.py or similar
# TODO: Improve help descriptions

# -t and -v interaction:
#
# t + v = everything
# t = just build lexicon
# v = ???
# _ = totally slient
#
# Here's how I want it to work:
# -a -b -d: generates AVL, Benchmark, and Dict
# -a filename -b filename -d filename: same but with custom filenames
#
# If none of -a -b -d present: make an AVL

import argparse
from src.lexicon.lexicon_avl import LexiconAVL
from src.lexicon.lexicon_dict import LexiconDict
from src.lexicon.lexicon_benchmark import LexiconBenchmark
from src.utils.test_utils import time_method

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
    # lexicon avl
    parser.add_argument(
        '-a', '--avl-tree', '--avl',
        help='Generates lexicon using AVL Tree',
        const='lexicon_avl.txt',
        type=str,
        nargs='?'
    )
    # lexicon dict
    parser.add_argument(
        '-d', '--dictionary', '--dict-test',
        help='Generates lexicon using dict',
        const='lexicon_dict.txt',
        type=str,
        nargs='?'
    )
    # lexicon benchmark
    parser.add_argument(
        # TODO: Add option to specify benchmark lexicon filename
        '-b', '--benchmark',
        help='Generate a benchmark lexicon',
        const='lexicon_benchmark.txt',
        type=str,
        nargs='?'
    )
    # time
    parser.add_argument(
        # TODO: Take an int as num of repeats
        '-t', '--time',
        help='Shows runtime',
        const=1,
        type=int,
        nargs='?'
    )
    # verbose
    parser.add_argument(
        '-v', '--verbose',
        help='Increases the amount of printed text',
        action='store_true'
    )
    # slow
    parser.add_argument(
        '-s', '--slow',
        help='Generates benchmark lexicon even slower',
        action='store_true'
    )
    # compare
    parser.add_argument(
        # TODO: Test
        # NOTE: Stores [] if -c with no args
        # Stores None if no -c
        '-c', '--compare', '--comp --cmp',
        help='Compares lexicon against benchmark lexicon',
        type=str,
        nargs='*'
    )

    return parser

def handle_build_lexicon(type: str, args: argparse.Namespace):

    match type:
        case 'avl':
            lexicon_type = LexiconAVL
        case 'dict':
            lexicon_type = LexiconDict
        case 'benchmark':
            lexicon_type = LexiconBenchmark
        case _:
            pass

    lexicon = lexicon_type()

    # TODO: Ugly, fix
    if args.time and not args.verbose:
        lexicon_args = [args.input_file, args.output_file, args.verbose]
    else:
        lexicon_args = [args.input_file, args.output_file, args.time, args.verbose]

    if lexicon_type == LexiconBenchmark:
        lexicon_args.append(args.slow)

    if args.time:
        time_method(lexicon.build_lexicon, *lexicon_args) # TODO: add N repeats from args.time
    else:
        lexicon.build_lexicon(*lexicon_args)

def handle_compare():
    pass

def handle_args(args: argparse.Namespace):
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
