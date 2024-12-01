#!/usr/bin/env python3

import argparse
import sys

# TODO: Move main method stuff here

def process_file(input_file, output_file, flags):
    '''
    Process the input file and save results to the output file.
    '''
    print(f'Processing file: {input_file}')
    print(f'Output will be saved to: {output_file}')
    print(f'Using flags: {flags}')
    # Add your file processing logic here
    print('Processing complete!')

def main():
    '''
    Main entry point for the script. Determines execution mode based on the presence of arguments.
    '''
    # Arguments provided, use argparse to parse them
    parser = argparse.ArgumentParser(description=f'Lexiconizer: Count wordsand find neighbours.')

    parser.add_argument('input_file', help='Input filename')
    parser.add_argument('output_file', help='Output filename')

    parser.add_argument(
        '-c', '--control',
        help='Generate a control lexicon',
        action='store_true'
    )

    # parser.add_argument('-s', '--slow', help='Generates control lexicon even slower')
    # parser.add_argument('-d', '--dict', '--dictionary', help='Generates lexicon using dict')
    # parser.add_argument('-t', '--time', help='Shows runtime')
    # parser.add_argument('-r', '--repeat', help='Repeats lexicon generation n times')
    # parser.add_argument('-v', '--verbose', help='Repeats lexicon generation n times')

    args = parser.parse_args()
    print(args)
    print(args.input_file)

    # # Validate and process the flags
    # validate_flags(args.flags)
    # process_file(args.input_file, args.output_file, args.flags)

if __name__ == '__main__':
    main()
