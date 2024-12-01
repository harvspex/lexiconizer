# from src.lexicon import Lexicon
from src.lexicon_avl import LexiconAVL
from tests.compare_lexicons import compare
from timeit import timeit

# TODO: Move methods and delete this file

# TODO: Move this somewhere else
def time_build_lexicon(
    lexicon: LexiconAVL,
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
    lexicon: LexiconAVL = LexiconAVL()

    time_build_lexicon(
        lexicon,
        input_filename,
        output_filename,
        repeats,
        compare_files=True
    )

if __name__ == '__main__':
    main()