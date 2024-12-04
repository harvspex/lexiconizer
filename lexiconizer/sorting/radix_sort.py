PAD_CHARACTER = ' '

def pad_string(string: str, key_length: int):
    """Right-pads a string with spaces up to a key length

    Args:
        string (str): The string to right-pad with spaces
        key_length (int): The length to pad the string to

    Returns:
        (str): The string right-padded with spaces, up to `key_length`
    """
    pad_amount: int = key_length - len(string)
    return f'{string}{PAD_CHARACTER * pad_amount}'


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
    if ch == PAD_CHARACTER:
        index = 0
    elif ch.islower():
        index = 1 + (ord(ch) - ord('a'))
    else:
        raise ValueError(f'Error. Unsupported character: {ch}')
    return index

def radix_sort(lst: list[str], key_length: int) -> list[str]:
    """Sorts a list inplace using radix sort

    Args:
        lst (list): The list to sort
        key_length (int): The length of the longest word (key)
    """

    # Set up the buckets
    buckets = [[] for _ in range(27)]

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

        # Copy elements back to list
        idx = 0
        for bucket in buckets:
            for string in bucket:
                lst[idx] = string
                idx += 1

    return [word.strip() for word in lst]
