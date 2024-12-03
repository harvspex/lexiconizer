# Lexiconizer
A refactor of my solution for the following requirements. Given a text input:
- Count the number of occurrences of each word.
- Find each word's list of "neighbours". A neighbour is any other word of the same length, which differs by only one character.
- Write this information to file. Both the lexicon and neighbour lists must each be in alphabetical order.
- The goal is to get the fastest runtime possible.
- To increase the difficulty, built-in sorting methods and data structures were not allowed. However, the optimisations still greatly enhance speed when using built-ins. A built-in version is provided for comparison.

## How it works
- Data is inserted into an AVL Tree (or a dictionary in the built-in version).
- The tree is traversed in order. Words are categorised based on length, and the first two letters.
- These categories are used to greatly minimize the number of comparisons needed to identify neighbours. 

## How to use
`lexiconizer [filename]`: run lexiconizer on the specified filename or file path. Outputs to "lexicon.txt"

Optional arguments:
- `--output-file` / `-o` / `-o [filename]`: specify the filename for the lexicon output.
- `--avl-tree` / `-a` / `-a [filename]`: generate using an AVL Tree (with optional output filename).
- `--dictionary` / `-d` / `-d [filename]`: generate using a dict (with optional output filename).
- `--benchmark` / `-b` / `-b [filename]`: generate a benchmark lexicon (with optional output filename).
- `--time` / `-t` / `-t [int]`: displays runtime. If a number is specified, repeats the program that many times, and displays the average runtime.
- `--verbose` / `-v`: Prints more information about specific steps being taken.
- `--compare` / `-c` / `-c [filenames]` compares the generated lexicons, and any number of specified files.

### Example Use:

`lexiconizer infile.txt -o my_lexicon -a -d -b -t 15 -v -c file_a file_b`

This will:
- Generate an AVL lexicon 15 times
  - Print each step
  - Print average runtime
  - Save to "my_lexicon_avl.txt"
- Generate a dict lexicon 15 times
  - Print each step
  - Print the average runtime
  - Save to "my_lexicon_dict.txt"
- Generate a benchmark lexicon 1 time*
  - Print each step
  - Print the runtime
  - Save to "my_lexicon_benchmark.txt"
- Compare all of the above files, along with file_a and file_b
  - Mismatched files will be printed to screen
  - Otherwise, prints "All files match."

*This only runs once because the benchmark lexicon is very slow for large inputs. The benchmark lexicon is provided to showcase how slowly neighbours are added with minimal optimisations.


## How to install
Complete...


## Optimisations
### AVL Tree
Lexiconizer begins by inserting words into an [AVL tree](https://en.wikipedia.org/wiki/AVL_tree). If the word is already present, then its frequency counter is increased instead.

After all words have been counted, the tree is traversed inorder, creating an ordered list of words. During traversal, words are also sorted into sublists. These sublists are then used for checking if a word is "neighbours" with another word. The benefit of using sublists is that the number of comparisons between words is significantly reduced, resulting in a faster runtime.

### Sublists
The rationale behind using sublists is as follows:

- For two words to be neighbours, they must be the same length
- For words longer than 1 letter, they must also:
    - Start with the same letter
    - Or have the same 2<sup>nd</sup> letter

If neither the 1<sup>st</sup> nor the 2<sup>nd</sup> letter match, then there are more than one different characters, meaning the words are not neighbours. Therefore, we can avoid time-consuming comparisons between a large number of words.

The way these sublists are populated and used preserves alphabetical order, eliminating the need for additional sorting.

### Time Complexity
### (Note: big O notation requires correction. Or delete this section)
- AVL insertion has a time complexity of O(log n) [n log n for n data points]
- AVL traversal has a time complexity of O(n) [or is it O(log n) ???]
- Checking neighbours has a time complexity of O(n(n-1)/2) [simplifies to O(n<sup>2</sup>)]

<!-- Talk about why AVL insertion is worth it due to lack of need for sorting -->

As checking neighbours has the largest time complexity, this is where the majority of optimisations occurred. These optimisations have resulted in insertion being the slowest part! Therefore, the overall, simplified time complexity is **O(log n)**

By reducing the pool of candidate neighbour words as greatly as possible, the negative effects of quadratic time are greatly diminished. Consider a list of all 3 letter "words":

`aaa aab aac ... zzx zzy zzz`

There are 17576 words
```
  n(n-1)/2
= 17576(17576−1)/2
= 154449100 comparisons
```
But by checking within subgroups:
- There are 676 words per subgroup with same first letter: `aaa aab aac ... azx azy azz`
- There are 676 words per subgroup with same second letter: `aaa aab aac ... zax zay zaz`

```
  n(n-1)/2
= 676(676−1)/2
= 228150 comparisons per subgroup

228150 * 52 subgroups = 11863800 comparisons
```
That's already 13 times fewer comparisons.

In practice, this number is reduced **even further.** After the first pass (checking words with the same 1<sup>st</sup> letter), the second pass only checks words with the same 2<sup>nd</sup> letter, and a 1<sup>st</sup> letter after that of the word being checked.

e.g. `abc` is checked against `bba, bbc, bbd ... zbx, zby, zbz`<br>
But skips checking `aba, abb, abc ... abx, aby, abz`

Also, as we already know that the first letter is different, and the second letter is the same, we only need to compare the remaining letters (until a difference is found). This reduces comparisons even further.

### EAFP
*"Easier to Ask for Forgiveness than Permission"*

Lexiconizer frequently "asks for forgiveness" (using try/except blocks) rather than "permission" (using comparisons). This is done for conditional statements that are reached infrequently.

Rather than running a comparison every time, Lexiconizer assumes the more likely condition, and manages the unlikely conditions handling the raised exception.

## Refactor
Compared to the original, the refactor:
- Runs from CLI, with various options
- Makes greater use of inheritance
- Makes more efficient use of data/memory (i.e. the same nested list is used for checking neighbours at index 0 and index 1, with more sophisticated traversal routines)
- Traversal of subgroups (for neighbour comparisons) have been reworked into concise recursive solutions

The core ideas and time complexity remain unchanged.