from src.lexicon import Lexicon
from tests.test_output import compare
from timeit import timeit

# TODO: Put in /src ?
# TODO: Make lexiconizer usable in one or both of these ways:
#   1. Calling it from cli with args `lexiconizer (infile) (outfile)`
#   2. Interactive CLI version using cmd library

def time_build_lexicon(
    lexicon: Lexicon,
    input_filename: str,
    output_filename: str='lexicon.txt',
    N_REPEATS: int=1,
    compare_files: bool=False
):
    print("\nRunning...")
    total_execution_time = timeit(
        lambda: lexicon.build_lexicon(input_filename, output_filename),
        globals=globals(),
        number=N_REPEATS
    )
    average_time = total_execution_time / N_REPEATS
    print("COMPLETE.")
    print(f'\nAverage execution time: {average_time:.2f}s across {N_REPEATS} runs')

    if compare_files:
        compare(test_filename=output_filename)

def main():
    input_filename: str = 'in.txt'
    output_filename: str = 'lexicon.txt'
    repeats: int = 1
    lexicon: Lexicon = Lexicon()
    time_build_lexicon(
        lexicon,
        input_filename,
        output_filename,
        repeats,
        compare_files=True
    )

if __name__ == '__main__':
    main()