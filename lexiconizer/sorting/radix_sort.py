"""A quick demo of radix sort to sort a list of strings made from upper case letters and spaces

Our buckets are:
    Bucket 0: ' ' (space character)
    Bucket 1-26: a-z (lower case characters)
"""


def find_key_length(lst):
    """Given a list of strings, finds the length of the longest string

    Args:
        lst (list of str): The list of strings

    Returns:
        (int): The length of the longest string in the list
    """
    max_length = 0

    for string in lst:
        string_length = len(string)
        if string_length > max_length:
            max_length = string_length

    return max_length


def pad_string(string, key_length):
    """Right-pads a string with spaces up to a key length

    Args:
        string (str): The string to right-pad with spaces
        key_length (int): The length to pad the string to

    Returns:
        (str): The string right-padded with spaces. The length of this string will = key_length
            (unless the string was initially longer than key_length)
    """
    for i in range(key_length - len(string)):
        string += ' '
    return string


def extract_character_for_pass(key, p):
    """Extracts the p'th character from the string key

    Args:
        key (str): String to extract character out of
        p (int): The current pass of radix sort. Used to know which character to extract

    Returns:
        (str): The extracted character
    """
    idx = len(key) - p
    return key[idx]


def get_character_bucket_index(ch: str):
    """Determines which bucket a character belongs to

    Buckets 0 is reserved for the 'space' character
    Buckets 1 - 26 are reserved for upper-case characters

    An exception is raised if we encounter an unsupported character

    We use ord() to get the decimal ascii value of a character

    Args:
        ch (str): Character to determine which bucket it belongs to

    Returns:
        (int): Index of the bucket the character belongs to
    """
    if ch == ' ':
        index = 0
    elif ch.islower():
        index = 1 + (ord(ch) - ord('a'))
    else:
        raise ValueError(f'Error. Unsupported character: {ch}')
    return index

def radix_sort(lst: list[str]):
    """Sorts a list inplace using radix sort

    This operates inplace, meaning the list will be sorted after calling this function

    Args:
        lst (list): The list to sort
    """
    # Create a list of 27 empty lists (used as our buckets)
    buckets = []
    for _ in range(27):
        buckets.append([])

    # Alternatively:
    # buckets = [[] for _ in range(27)]

    # Determine the length of the longest string, this is the key length
    key_length = find_key_length(lst)

    # Right pad all strings with the space character (up to the key length)
    for string_idx in range(len(lst)):
        lst[string_idx] = pad_string(lst[string_idx], key_length)

    # Perform radix sort passes. Number of passes = the key length
    for pass_num in range(1, key_length + 1):
        # Empty the buckets
        for bucket in buckets:
            bucket.clear()

        # Put elements in buckets based on digit value
        for string in lst:
            ch = extract_character_for_pass(string, pass_num)
            bucket_idx = get_character_bucket_index(ch)
            buckets[bucket_idx].append(string)

        # # Display buckets for inspection
        # print(f'\nPass Number: {pass_num}')
        # for bucket_idx, bucket in enumerate(buckets):
        #     print(f'Bucket {bucket_idx}: {bucket}')

        # Copy elements back to list
        idx = 0
        for bucket in buckets:
            for string in bucket:
                lst[idx] = string
                idx += 1

    return [word.strip() for word in lst]
