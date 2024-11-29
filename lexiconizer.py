import sys

# TODO: Move main method stuff here
# If 2 args, and both are valid file paths: create lexicon
# If no args, run interactive cli version
# Otherwise, print error message.

def example():
    # total arguments
    n = len(sys.argv)
    print("Total arguments passed:", n)

    # Arguments passed
    print("\nName of Python script:", sys.argv[0])

    print("\nArguments passed:", end = " ")
    for i in range(1, n):
        print(sys.argv[i], end = " ")
        
    # Addition of numbers
    Sum = 0
    # Using argparse module
    for i in range(1, n):
        Sum += int(sys.argv[i])
        
    print("\n\nResult:", Sum)

def main():
    example()

if __name__ == '__main__':
    main()