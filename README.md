# Lexiconizer
A refactor of my solution for the following puzzle. Given a text input:
- Count the number of occurrences of each word.
- Find each word's list of "neighbours". A neighbour is any other word of the same length, which differs by only one character.
- Write this information to file. The lexicon and neighbour-lists must each be in alphabetical order.
- The goal is to get the fastest possible runtime.
- To increase the difficulty, **built-in sorting methods and data structures were not allowed.**

## AVL Tree
Lexiconizer begins by inserting words into an [AVL tree](https://en.wikipedia.org/wiki/AVL_tree). If the word is already present, then its frequency counter is increased instead.

After all words have been counted, the tree is traversed inorder, creating an ordered list of words. During traversal, words are also sorted into sublists. These sublists are then used for comparing if a word is "neighbours" with another word. The benefit of using sublists is that the number of comparisons between words is significantly reduced, resulting in a faster runtime.

## Nested lists
The rationale behind using sublists is as follows:

- For two words to be neighbours, they must be the same length
- For words longer than 1 letter, they must also:
    - Start with the same letter
    - Or have the same 2<sup>nd</sup> letter

If neither the 1<sup>st</sup> nor the 2<sup>nd</sup> letter match, then there are more than one different characters, meaning the words are not neighbours. Therefore, we can avoid time-consuming comparisons between words that:

- Are different lengths
- Start with 2 completely different letters

The way these sublists are populated and used preserves alphabetical order, eliminating the need for additional sorting.