from timeit import timeit
from typing import Callable
import filecmp

# TODO: Docstrings

def compare_files(filenames: list[str], shallow=False) -> bool:
    """
    Compares the contents of multiple files to check if they match.

    This function iterates through pairs of files from the given list and 
    compares their contents. If any mismatch is found, a message is printed 
    indicating the files that differ. If all files match, a confirmation 
    message is printed.

    Prints error message if the number of files in the `filenames` is less 
    than 2.

    Args:
        filenames (list[str]): A list of file paths to compare.
        shallow (bool): Whether to perform a shallow comparison 
            (Default: False).

    Returns:
        bool: True if all files match, False if any mismatch is found.
    """
    files_match: bool = True
    len_filenames = len(filenames)

    if len_filenames < 2:
        print('Can\'t compare less than 2 files.')
        return

    for a in range(len_filenames):
        file_a = filenames[a]

        for b in range(a+1, len_filenames):
            file_b = filenames[b]

            if not filecmp.cmp(file_a, file_b):
                files_match = False
                print(f'File mismatch found:\n  {file_a}\n  {file_b}')

    if files_match:
        print('All files match.')

    return files_match

def time_method(
        method: Callable,
        *args,
        n_repeats: int=1,
        verbose: bool=False,
        print_message: str=None,
        **kwargs
):
    """
    Measure the runtime of a callable function over multiple repeats.

    This function uses the `timeit` module to calculate the total 
    execution time of the provided `build_lexicon` function, called with
    the specified positional (`*args`) and keyword arguments 
    (`**kwargs`). It repeats the execution for a given number of times 
    (`n_repeats`) and optionally prints detailed output if `verbose` is 
    set to `True`.

    Args:
        build_lexicon (Callable): The function to be executed and timed.
        *args: Positional arguments to be passed to `build_lexicon`.
        n_repeats (int, optional): The number of times to repeat the 
            execution (default: 1).
        verbose (bool, optional): If `True`, prints detailed output, 
            including function name and average execution time. 
            (default: False).
        **kwargs: Keyword arguments to be passed to `build_lexicon`.

    Prints:
        If `verbose` is `True`, prints the function name, number of 
        repetitions, and the average execution time. If `verbose` is 
        `False`, prints only the average execution time.

    Example:
        >>> def example_function(a, b):
        ...     return a + b
        >>> time_method(example_function, 1, 2, n_repeats=5, 
        verbose=True)
        Running example_function 5 times...
        COMPLETE. Average execution time: 0.00s across 5 runs
    """
    total_execution_time = timeit(lambda: method(*args, **kwargs), number=n_repeats)
    average_time = f'{total_execution_time / n_repeats:.2f}s'

    if verbose:
        amount: str = 'total' if (n_repeats == 1) else 'average'
        print_message: str = f'Finished with {amount} runtime: {average_time}\n'
        print(print_message)

    else:
        print(average_time)
