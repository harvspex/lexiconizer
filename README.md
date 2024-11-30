# Lexiconizer
A refactor of my solution for the following requirements. Given a text input:
- Count the number of occurrences of each word.
- Find each word's list of "neighbours". A neighbour is any other word of the same length, which differs by only one character.
- Write this information to file. Both the lexicon and neighbour-lists must each be in alphabetical order.
- Reduce the runtime as greatly as possible.
- To increase the difficulty, **built-in sorting methods and data structures were not allowed.**
  - The optimisations still greatly enhance speed when using built-ins. A built-in version is provided for comparison.

## At a glance
- Data is inserted into an AVL Tree (or a dictionary in the built-in version).
- The tree is traversed in order. Words are categorised based on length, and the first two letters.
- These categories are used to greatly minimize the number of comparisons needed to identify neighbours. 

## AVL Tree
Lexiconizer begins by inserting words into an [AVL tree](https://en.wikipedia.org/wiki/AVL_tree). If the word is already present, then its frequency counter is increased instead.

After all words have been counted, the tree is traversed inorder, creating an ordered list of words. During traversal, words are also sorted into sublists. These sublists are then used for checking if a word is "neighbours" with another word. The benefit of using sublists is that the number of comparisons between words is significantly reduced, resulting in a faster runtime.

## Nested lists
The rationale behind using sublists is as follows:

- For two words to be neighbours, they must be the same length
- For words longer than 1 letter, they must also:
    - Start with the same letter
    - Or have the same 2<sup>nd</sup> letter

If neither the 1<sup>st</sup> nor the 2<sup>nd</sup> letter match, then there are more than one different characters, meaning the words are not neighbours. Therefore, we can avoid time-consuming comparisons between a large number of words.

The way these sublists are populated and used preserves alphabetical order, eliminating the need for additional sorting.

## Time Complexity (Note: big O notation requires correction. Or delete this section)
- AVL insertion has a time complexity of O(log n)
- AVL traversal has a time complexity of O(n)
- Checking neighbours has a time complexity of O(n(n-1)/2) [simplifies to O(n<sup>2</sup>)]

As checking neighbours has the largest time complexity, this is where the majority of optimisations occurred. These optimisations have resulted in insertion being the slowest part! Therefore, the overall, simplified time complexity is **O(log n)**

By reducing the pool of candidate neighbour words as greatly as possible, the negative effects of quadratic time are greatly diminished. Consider the following "lexicon":
`aa ab ac ba bb bc ca cc cb`

The number of comparisons needed to check neighbours would be 36
```
  n(n-1)/2
= 9(9-1)/2
= 36 comparisons
```
But by checking within subgroups:
- Words with same first letter subgroups: `aa ab ac` `ba bb bc` `ca cc cb`
- Words with same second letter subgroups: `aa ba ca` `ab bb cb` `ac bc cc`

```
  n(n-1)/2
= 3(3-1)/2
= 3 comparisons per subgroup

3 comparisons * 6 subgroups = 18 total comparisons
```

<!-- Pick a larger number of words for a more interesting result. e.g. all 3 letter words -->
The reduction scales based on the size of the lexicon relative to the size of subgroups. Assuming a complete set of 2 letter "words": `aa, ab, ac, ad... zx, zy, zz`
- There are 676 words
- The number of comparisons without subgroups is **228,150**
- The number of comparisons with subgroups is **16,900**

In practice, this number is reduced **even further.** After the first pass (checking words with the same 1<sup>st</sup> letter), the second pass only checks words with the same 2<sup>nd</sup> letter, and a 1<sup>st</sup> letter after that of the word being checked.

e.g. `abc` is checked against `bba, bbc, bbd ... zbx, zby, zbz`<br>
But skips checking `aba, abb, abc ... abx, aby, abz`

Because we already know that the first letter is different, and the second letter is the same, we only need to compare the remaining letters (until a difference is found). This reduces comparisons even further.

## EAFP
*"Easier to Ask for Forgiveness than Permission"*

Lexiconizer frequently "asks for forgiveness" (using try/except blocks) rather than "permission" (using comparisons). This is done for conditional statements that are reached infrequently.

Rather than running a comparison every time, Lexiconizer assumes the more likely condition, and handles the unlikely conditions using raised exception.

## Refactor
Compared to the original, the refactor:
- Makes greater use of inheritance
- Makes more efficient use of data/memory (i.e. the same nested list is used for checking neighbours at index 0 and index 1, with more sophisticated traversal routines)
- Traversal of subgroups (for neighbour comparisons) have been reworked into concise recursive solutions

The core ideas and time complexity remain unchanged.