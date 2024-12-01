# TODO

## Lexicon
- init with filename?
    - for control lexicon too
- add option to time individual methods
- add verbose option
- Handle IOError if files cannot be read

## CLI
- Move main method stuff to lexiconizer
    - Create CLI versions
        - CLI flags (e.g. dict mode, AVL mode, flags for tests)
    - Delete main.py
    - Move timeit stuff somewhere else
- Could make interactive CLI version if no args provided

## Testing
- Unit test cases (e.g. check neighbours)
- Check old assignment for implementations of radix, quick, tim sort
    - Can compare to sorted version
- Test case for ControlLexicon
- merge test_lexicon_dict elsewhere

## Misc
- Consider: change same_char_0 -> first_letter

## Docstrings
- lexicon_avl.py
- lexicon_dict.py
- lexicon.py
- control_lexicon.py
- same_char_1_utils.py
- test utils

## Performance
- neighbour_utils.py
    - Check len(spelling_a) impact on runtime
    - Can end be passed into word_is_neighbours based on the index of the current list?
        - also for same_char_1_utils.py