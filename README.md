# Lexiconizer
A refactor of my solution for the following puzzle. Given a text input:
- Count the number of occurrences of each word.
- Find each word's list of "neighbours". A neighbour is any other word of the same length, which differs by only one character.
- Write this information to file. The lexicon and neighbour-lists must each be in alphabetical order.
- The goal is to get the fastest possible runtime.
- To increase the difficulty, **built-in sorting methods were not allowed.**

## AVL Tree
Lexiconizer begins by inserting words into an [AVL tree](https://en.wikipedia.org/wiki/AVL_tree). If the word is already present, then its frequency counter is increased instead.

After all words have been counted, the tree is traversed inorder, creating an ordered list of words. During traversal, words are also sorted into sublists. These sublists are then used for checking if a word is "neighbours" with another word. The benefit of using sublists is that the number of comparisons between words is significantly reduced, resulting in a faster runtime.

## Nested lists
The rationale behind using sublists is as follows:

- For two words to be neighbours, they must be the same length
- For words longer than 1 letter, they must also:
    - Start with the same letter
    - Or have the same 2<sup>nd</sup> letter

If neither the 1<sup>st</sup> nor the 2<sup>nd</sup> letter match, then there are more than one different characters, meaning the words are not neighbours. Therefore, we can avoid time-consuming comparisons between words that:

- Are different lengths
- Start with 2 completely different letters

The way these sublists are populated and used also preserves alphabetical order, eliminating the need for additional sorting.

## Time Complexity
- AVL insertion has a time complexity of O(log n)
- AVL traversal has a time complexity of O(n)
- Checking neighbours has a time complexity of O(n(n-1)/2). This simplifies to O(n<sup>2</sup>)

As checking neighbours has the largest time complexity, this is where the majority of optimisations occurred. By reducing the pool of candidate neighbour words as greatly as possible without making individual comparisons, the negative effects of quadratic time are greatly diminished.

Consider the following "lexicon":
`aa ab ac ba bb bc ca cc cb`

The number of comparisons needed to check neighbours would be 36
```
n(n-1)/2 = 9(9-1)/2 = 36 comparisons
```
But by checking within subgroups:
- Words with same first letter: `aa ab ac` `ba bb bc` `ca cc cb`
- Words with same second letter: `aa ba ca` `ab bb cb` `ac bc cc`

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
- In practice, this number is reduced even further by other logical optimisations