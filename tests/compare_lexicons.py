import filecmp

def compare(
    test_filename: str='lexicon.txt',
    control_filename:str='control_lexicon.txt',
    shallow=False
) -> bool:
    result = filecmp.cmp(test_filename, control_filename, shallow=shallow)
    print(f'Files match: {result}')
    return result
