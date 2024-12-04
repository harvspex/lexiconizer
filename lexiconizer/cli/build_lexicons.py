import os
from typing import Callable
from lexiconizer.lexicons.lexicon import Lexicon
from lexiconizer.lexicons.lexicon_dict import LexiconDict
from lexiconizer.lexicons.lexicon_benchmark import LexiconBenchmark
from lexiconizer.utils.test_utils import time_method
from lexiconizer.cli.lexicon_type import LexiconType


def build_all_lexicons(
    input_file: str,
    output_file: str,
    time: int,
    verbose: bool,
    lexicon_types: list[LexiconType]
) -> list[str]:

    # Prepare default filename and extension
    default_filename, extension = os.path.splitext(output_file)
    if extension == '':
        extension = '.txt'

    filenames: list[str] = []

    # Build each lexicon, adding filename to `filenames`
    for l_type in lexicon_types:
        filename: str

        match l_type.filename:
            case None:
                continue
            case l_type.name:
                filename = f'{default_filename}_{l_type.name}{extension}'
            case _:
                filename, sub_extension = os.path.splitext(l_type.filename)
                filename += extension if sub_extension is None else sub_extension

        build_one_lexicon(
            input_file=input_file,
            output_file=filename,
            lexicon_type=l_type,
            n_repeats=time,
            verbose=verbose,
        )
        filenames.append(filename)

    # Build a default lexicon if none specified
    if not filenames:
        filename: str = default_filename + extension
        l_type: LexiconType = next(
            (lt for lt in lexicon_types if lt.name == 'default'),
            lexicon_types[0]
        )

        build_one_lexicon(
            input_file=input_file,
            output_file=filename,
            lexicon_type=l_type,
            n_repeats=time,
            verbose=verbose
        )
        filenames.append(filename)

    return filenames


def build_one_lexicon(
    input_file: str,
    output_file: str,
    lexicon_type: LexiconType,
    n_repeats: int,
    verbose: bool,
):
    # Create lexicon
    lexicon: Lexicon
    if lexicon_type.sorting_method is not None:
        lexicon = lexicon_type.lexicon_type(lexicon_type.sorting_method)
    else:
        lexicon = lexicon_type.lexicon_type()

    # Prepare args for `lexicon.build_lexicon`
    time_lexicon: bool = n_repeats is not None
    time_methods: bool = False if (time_lexicon and not verbose) else time_lexicon
    build_lexicon_args = [input_file, output_file, verbose, time_methods]

    # Prepare print message
    lexicon_name: str = lexicon_type.name.upper().replace("_", " ")
    print_message: str = f'Building {lexicon_name} lexicon'
    ellipsis: str = '...'

    # Build lexicon without timing
    if not time_lexicon:
        if verbose:
            print_message += ellipsis
            print(print_message)
        lexicon.build_lexicon(*build_lexicon_args)
        return

    # n_repeats is always 1 for LexiconBenchmark
    if lexicon_type.lexicon_type is LexiconBenchmark:
        n_repeats = 1

    # Add repeats to print message
    print_amount: str = f' {n_repeats} times{ellipsis}'
    print_message += ellipsis if (n_repeats == 1) else print_amount
    print(print_message)

    # Build lexicon and display time
    time_method(
        lexicon.build_lexicon,
        *build_lexicon_args,
        n_repeats=n_repeats,
        verbose=True
    )