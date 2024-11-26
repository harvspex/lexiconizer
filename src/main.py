from lexicon import Lexicon
from timeit import timeit

def time_build_lexicon(lexicon: Lexicon, input_filename: str, output_filename: str='out.txt', N_REPEATS: int=1):
    print("\nRunning...")
    total_execution_time = timeit(lambda: lexicon.build_lexicon(input_filename, output_filename), globals=globals(), number=N_REPEATS)
    average_time = total_execution_time / N_REPEATS
    print("COMPLETE.")
    print(f'\nAverage execution time: {average_time:.2f}s across {N_REPEATS} runs')

def main():
    filename = 'in.txt'
    lexicon = Lexicon()
    # TODO: for N_REPEATS > 1 out recounts the lexicon and extends the output. Fix that
    time_build_lexicon(lexicon, filename, 'out.txt', 1)

if __name__ == '__main__':
    main()