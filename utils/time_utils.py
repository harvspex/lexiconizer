from timeit import timeit
from typing import Callable

def time_method(
        build_lexicon: Callable,
        *args,
        n_repeats: int=1,
        verbose: bool=False,
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
    if verbose: print(f'Running {build_lexicon.__name__} {n_repeats} times...')

    total_execution_time = timeit(lambda: build_lexicon(*args, **kwargs), number=n_repeats)
    average_time = f'{total_execution_time / n_repeats:.2f}s'

    if verbose: print(f'COMPLETE. Average execution time: {average_time} across {n_repeats} runs')
    else: print(average_time)