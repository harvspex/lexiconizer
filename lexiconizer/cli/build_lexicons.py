import os
from typing import Callable

from lexicons.lexicon import Lexicon
from lexicons.lexicon_dict import LexiconDict
from lexicons.lexicon_benchmark import LexiconBenchmark
from utils.test_utils import time_method
from cli.lexicon_type import LexiconType


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
            filename=filename,
            lexicon_type=l_type.lexicon_type,
            n_repeats=time,
            verbose=verbose,
            sorting_method=l_type.sorting_method
        )
        filenames.append(filename)

    # Build a default lexicon if none specified
    if not filenames:
        filename = default_filename + extension
        build_one_lexicon(
            input_file=input_file,
            filename=filename,
            lexicon_type=LexiconDict,
            n_repeats=time,
            verbose=verbose
        )
        filenames.append(filename)

    return filenames


def build_one_lexicon(
    input_file: str,
    filename: str,
    lexicon_type: type,
    n_repeats: int,
    verbose: bool,
    sorting_method: Callable=None
):
    # TODO: If verbose, print lexicon type (not "running build_lexicon")

    lexicon: Lexicon

    if sorting_method is not None:
        lexicon = lexicon_type(sorting_method)
    else:
        lexicon = lexicon_type()

    time_lexicon: bool = n_repeats is not None
    time_methods: bool = False if (time_lexicon and not verbose) else time_lexicon
    build_lexicon_args = [input_file, filename, verbose, time_methods]

    # Build lexicon without timing
    if not time_lexicon:
        lexicon.build_lexicon(*build_lexicon_args)
        return

    # Print average time if n_repeats > 1
    print_average: bool = True if (n_repeats > 1) else False

    # n_repeats is always 1 for LexiconBenchmark
    if lexicon_type is LexiconBenchmark: n_repeats = 1

    # Build lexicon and display time
    time_method(
        lexicon.build_lexicon,
        *build_lexicon_args,
        n_repeats=n_repeats,
        verbose=print_average
    )
