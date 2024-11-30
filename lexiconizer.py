#!/usr/bin/env python3

import argparse
import sys

# TODO: Move main method stuff here
# If 2 args, and both are valid file paths: create lexicon
# If no args, run interactive cli version
# Otherwise, handle error.

def main_menu():
    """
    Interactive CLI mode when the script is run without arguments.
    """
    print("Welcome to Lexiconize!")
    print("Please choose an option:")
    print("1. Process a file")
    print("2. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        input_file = input("Enter the input filename: ").strip()
        output_file = input("Enter the output filename: ").strip()
        flags = input("Enter any flags separated by space (or press Enter for none): ").strip().split()
        validate_flags(flags)
        process_file(input_file, output_file, flags)
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main_menu()


def validate_flags(flags):
    """
    Validate provided flags against the list of allowed options.
    """
    valid_flags = {"-c", "--control", "-s", "--slow", "-d", "--dict"}
    for flag in flags:
        if flag not in valid_flags:
            print(f"Invalid flag: {flag}")
            print(f"Allowed flags are: {', '.join(valid_flags)}")
            sys.exit(1)


def process_file(input_file, output_file, flags):
    """
    Process the input file and save results to the output file.
    """
    print(f"Processing file: {input_file}")
    print(f"Output will be saved to: {output_file}")
    print(f"Using flags: {flags}")
    # Add your file processing logic here
    print("Processing complete!")


def main():
    """
    Main entry point for the script. Determines execution mode based on the presence of arguments.
    """
    if len(sys.argv) == 1:
        # No arguments provided, enter interactive mode
        main_menu()
    else:
        # Arguments provided, use argparse to parse them
        parser = argparse.ArgumentParser(description="Lexiconize - A tool for processing files.")
        parser.add_argument("input_file", help="Input filename")
        parser.add_argument("output_file", help="Output filename")
        parser.add_argument(
            "flags",
            nargs="*",
            help="Optional flags for processing",
            choices=["-c", "--control", "-s", "--slow", "-d", "--dict"],  # Restrict valid flags
        )
        args = parser.parse_args()

        # Validate and process the flags
        validate_flags(args.flags)
        process_file(args.input_file, args.output_file, args.flags)


if __name__ == "__main__":
    main()
