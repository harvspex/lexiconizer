PAD_CHARACTER: str = ' ' # Used to pad keys (words) up to max word length
RADIX: int = 27 # The number of allowed characters, including pad character

def pad_string(string: str, key_length: int, pad_character: str=PAD_CHARACTER):
    """
    Right-pads a string with spaces up to key length

    Args:
        string (str): The string to right-pad with spaces
        key_length (int): The length to pad the string to

    Returns:
        (str): The string right-padded with spaces, up to `key_length`
    """
    pad_amount: int = key_length - len(string)
    return f'{string}{pad_character * pad_amount}'

def get_bucket_index(key: str, pass_num: int, pad_character: str=PAD_CHARACTER):
    """
    Determines which bucket a character belongs to.

    Buckets 0 is reserved for the 'padding' character
    Buckets 1 - 26 are reserved for lower case letters

    Args:
        key (str): The word (key) to extract bucket index from
        p (int): The current radix sort pass number. Used to get char
            from key
        pad_character (str, optional): the character used for padding
            during radix sort (default: PAD_CHARACTER=' ')

    Returns:
        (int): Index of the bucket the character belongs to

    Raises:
        ValueError: If ch is an unsupported character.
    """
    idx = len(key) - pass_num
    char = key[idx]

    if char == pad_character:
        index = 0
    elif char.islower():
        index = 1 + (ord(char) - ord('a'))
    else:
        raise ValueError(f'Error. Unsupported character: {char}')

    return index


def get_empty_buckets(radix: int=RADIX) -> list:
    """
    Get a list of lists. The number of sublists corresponds to the `radix`.

    Args:
        radix (int, optional): the radix. (default=RADIX)
    
    Returns:
        A list with containing `radix` number of empty sublists
    """
    return [[] for _ in range(radix)]


def radix_sort(lst: list[str], key_length: int, pad_character: str=PAD_CHARACTER) -> list[str]:
    """
    Sorts a list using radix sort

    Args:
        lst (list): The list to sort
        key_length (int): The length of the longest word (key)
        pad_character (str, optional): the character used for padding
            during radix sort (default: PAD_CHARACTER=' ')

    Returns:
        A list sorted using radix sort.
    """
    if pad_character != ' ':
        raise ValueError(f'Error: Currently, only " " (an empty space) is supported as a pad character')

    # Right pad all strings with the pad character (up to the key length)
    lst = [pad_string(string, key_length) for string in lst]
    buckets: list[list] = get_empty_buckets()

    # Perform radix sort passes. Number of passes = the key length
    for pass_num in range(1, key_length+1):
        buckets = get_empty_buckets()

        # Put elements in buckets based on digit value
        for string in lst:
            bucket_idx = get_bucket_index(string, pass_num)
            buckets[bucket_idx].append(string)

        # Recreate list using new order of elements in buckets
        lst.clear()
        for bucket in buckets:
            lst.extend(bucket)

    # Remove padding from words and return sorted list
    return [word.strip() for word in lst]
