import argparse
import os

def positive_int(value):
    """
    Validates and converts a string value to a positive integer.

    Args:
        value (str): The input value to validate.

    Returns:
        int: The validated positive integer.

    Raises:
        argparse.ArgumentTypeError: If the value is not a valid positive
            integer.
    """
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(
                f'Invalid value: {value}. Must be an integer greater than 0.'
            )
        return ivalue

    except ValueError:
        raise argparse.ArgumentTypeError(
            f'Invalid value: {value}. Must be an integer.'
        )


def readable_file(filepath):
    """
    Validates that the given filepath exists and is readable.

    Args:
        filepath (str): The path to the file.

    Returns:
        str: The filepath if it is valid and readable.

    Raises:
        argparse.ArgumentTypeError: If the file does not exist or is not
            readable.
    """
    if not os.path.isfile(filepath):
        raise argparse.ArgumentTypeError(
            f'"{filepath}" does not exist or is not a valid file.'
        )
    if not os.access(filepath, os.R_OK):
        raise argparse.ArgumentTypeError(
            f'"{filepath}" is not readable.'
        )
    return filepath


def writeable_file(filepath):
    """
    Validates that the given filepath is writable or can be created.

    Args:
        filepath (str): The path to the file.

    Returns:
        str: The filepath if it is valid and writable.

    Raises:
        argparse.ArgumentTypeError: If the file or its directory is not 
            writable.
    """
    # Check if the file exists
    if os.path.exists(filepath):
        if not os.path.isfile(filepath):
            raise argparse.ArgumentTypeError(
                f'"{filepath}" exists but is a directory.'
            )
        if not os.access(filepath, os.W_OK):
            raise argparse.ArgumentTypeError(
                f'"{filepath}" exists but is not writable.'
            )
    else:
        # File does not exist, check if the directory is writable
        parent_dir = os.path.dirname(filepath) or '.'
        if not os.access(parent_dir, os.W_OK):
            raise argparse.ArgumentTypeError(
                f'"{filepath}" cannot be created. The directory "{parent_dir}" is not writable.'
            )
    return filepath