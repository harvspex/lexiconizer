# TODO

## CLI
Current args:
input_file  (required)
output_file (required: try to make optional)
avl-tree
dictionary
benchmark
time
verbose
compare

- Add .txt to files (unless user-defined without .txt)
- Print lexicon type in verbose mode
- Could make interactive CLI version if no args provided
- add a "no reset" flag

-t and -v interaction:
t + v = everything
t = just build lexicon
v = just verbose
_ = totally slient

## Lexicon
- fix *args hacky thing
- Handle IOError if files cannot be read

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