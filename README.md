# Lexiconizer
A refactor of my solution to the following programming puzzle. Given a text input:
- Count the number of occurrences of each word.
- Find each word's list of "neighbours". A neighbour is any other word of the same length, which differs by only one character.
- Write this information to file. Both the lexicon and neighbour lists must each be in alphabetical order.
- The goal is to get the fastest runtime possible.
- To increase the difficulty, built-in sorting methods and data structures were not allowed. However, the optimisations still greatly enhance speed, even when using built-ins. Options using built-ins are provided for comparison.


## How it works
- Word data is read and sorted using the specified method
- After (or sometimes during) sorting, words are categorized into sublists based on certain criteria
- These sublists greatly minimize the number of comparisons needed to identify neighbours

More information under "Optimisations".


## How to use
Lexiconizer can be run in "portable mode" by navigating to the lexiconizer/ directory and running `python lexiconizer [args]`

<!-- TODO: Complete. It can also be installed, using... -->

### List of Options
```
input_file            filename or path of file to be lexiconized

-o, --output-file     specify the filename or path for output lexicon/s
-d, --default         generate lexicon using built-in `sorted` method
-q, --quicksort       generate lexicon using quicksort
-r, --radix-sort,     generate lexicon using radix sort
-a, --avl-tree        generate lexicon using AVL tree
-b, --benchmark       generate a "benchmark" lexicon (has minimal optimisations
                      for adding neighbours)
-t, --time            show runtime (optional: number of times to repeat lexicon
                      generation, for more accurate average runtime)
-v, --verbose         print the individual steps during lexicon generation (and
                      its runtime if using `-t`)
-c, --compare         compare all generated lexicons (optional: any number of
                      other filenames for comparison)

All lexicon methods [-d -q -r -a -b] optionally take a specific filename for
that lexicon. (e.g. `-d default_lexicon.txt`)
```


### Example Use:
`lexiconizer meditations.txt`
- Generates a default lexicon using "meditations.txt"
- Saves to "lexicon.txt" (default filename)

`lexiconizer "moby dick.txt" -o "moby dick lexicon.txt" -t -v`
- Generates a default lexicon using "moby dict.txt"
- `-v` prints individuals steps and `-t` prints their runtime
- `-t` also prints the total runtime
- `-o` saves output to "moby dick lexicon.txt"

`lexiconizer my_diary.txt -q diary_1.txt -r diary_2.txt -c diary_3.txt diary_4.txt`
- `-q` generates a quicksort lexicon and saves to "diary_1.txt"
- `-r` generates a radix sort lexicon and saves to "diary_2.txt"
- `-c` compares the newly generated "diary_1.txt" and "diary_2.txt", and the specified "diary_3.txt" and "diary_4.txt"
- `-c` prints "all files match" if so, otherwise prints mismatched files

`lexiconizer war_and_peace.txt -o my_lexicon.txt -d -a -b -t 15`
- `-d` generates a default lexicon
  - `-t` repeats this 15 times and prints the average runtime
  - `-o` saves to "my_lexicon_default.txt" ("default" is automatically added to prevent overwriting)
- `-a` generates an AVL lexicon 15 times
  - `-t` repeats this 15 times and prints the average runtime
  - `-o` saves to "my_lexicon_avl_tree.txt" ("avl_tree" is automatically added to prevent overwriting)
- `-b` generates a benchmark lexicon
  - `-t` repeats this 1 time* and prints the runtime
  - `-o` saves to "my_lexicon_benchmark.txt" ("benchmark" is automatically added to prevent overwriting)

*This only runs once because the benchmark lexicon is very slow, to highlight the effect of optimisations in other lexicons.


## Optimisation
Many optimisations have been made, with some specific to just one of the available options. However, each option (aside from the benchmark) uses the same technique to check for neighbours. 

Checking neighbours has a time complexity of O(n<sup>2</sup>) - that's not good! This is because each word needs to be checked against each other word, resulting in n(n-1)/2 operations (where n is the number of words). However, optimisations have reduced the impact so greatly, that for all tested inputs it beats the avl tree's insertion phase: O(n log n)

This was achieved by reducing the number of comparisons. A "neighbour" is defined as any other word of the same length, which differs by only one character. Therefore, another word cannot be neighbours if:
- It is a different length
- Both the first and the second letters don't match (i.e. there are more than one differences)

With these rules, we can avoid time-consuming comparisons between a large number of words. During sorting, words are appended to a deeply nested list, with an order corresponding to length, then the second letter, and finally the first letter. These these smaller subgroups greatly reduce the number of comparisons that need to be made. Additionally, the way that they are traversed:
- Avoids re-checking any two words that have already been checked
- Preserves alphabetical order for neighbour lists (no need for additional sorting!)
- Begins checking from the first letter that may be different (e.g. the third letter, if we know that the second is the same)

To showcase the impact of these optimisations, an option to make a "benchmark" lexicon has been included. Rather than using sublists, it treats every subsequent word in the lexicon as a potential neighbour. The benchmark still:
- Avoids re-checking any two words that have already been checked
- Rejects words as quickly as possible (e.g. if their length is different, or neither of the first two letters match, the two words are not compared any further)
- Uses built-in sorting methods to make everything else run as quickly as possible

But even these small comparison adds up. A word of warning: the benchmark can be very slow (e.g. ~30s for a 4.5mb text file). For this reason, it only runs once, even if the `--time` option specifies a number greater than 1.


## Refactor
Compared to the original, the refactor:
- Can be installed, and runs from CLI with various options
- Contains multiple ways of generating a lexicon, using various data structures or sorting algorithms
- Makes more efficient use of memory (e.g. the nested list used for checking neighbours)
- Traversal of subgroups (for neighbour comparisons) have been made more concise using recursion

The core ideas and approximate runtime remain unchanged.