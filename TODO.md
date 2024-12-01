# TODO

## Notes
Current args:
input_file
output_file
generate (control lexicon)
compare
slow
dictionary
time
verbose

t + v = everything
t = just build lexicon
v = ???
_ = totally slient

Here's how I want it to work:
-a -b -d: generates AVL, Benchmark, and Dict
-a filename -b filename -d filename: same but with custom filenames

If none of -a -b -d present: make an AVL

## Lexicon
- init with filename?
    - for control lexicon too
- add option to time individual methods
- add verbose option
- Handle IOError if files cannot be read
- fix *args hacky thing

## CLI
- Move main method stuff to lexiconizer
    - Create CLI versions
        - CLI flags (e.g. dict mode, AVL mode, flags for tests)
    - Delete main.py
    - Move timeit stuff somewhere else
- Could make interactive CLI version if no args provided
- add a "no reset" flag

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
- func class

## Performance
- neighbour_utils.py
    - Check len(spelling_a) impact on runtime
    - Can end be passed into word_is_neighbours based on the index of the current list?
        - also for same_char_1_utils.py