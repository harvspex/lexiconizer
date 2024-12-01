#!/usr/bin/env python3

import argparse
import sys

# TODO: Move main method stuff here?

def process_file(input_file, output_file, flags):
    print(f'Processing file: {input_file}')
    print(f'Output will be saved to: {output_file}')
    print(f'Using flags: {flags}')
    # Add your file processing logic here
    print('Processing complete!')


def main():
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
        '-t', '--time',
        help='Shows runtime',
        action='store_true'
    )

    # repeat
    parser.add_argument(
        '-r', '--repeat',
        help='Repeats lexicon generation n times',
        action='store_true'
    )

    # verbose
    parser.add_argument(
        '-v', '--verbose',
        help='Increases the amount of printed text',
        action='store_true'
    )

    args = parser.parse_args()
    print(args)
    print(args.input_file)


if __name__ == '__main__':
    main()
