from typing import Callable

def map_to_nested_list(nested_list: list, map_function: Callable, start: int=0, end: int=None):
    if end is None: end = len(nested_list)

    for i in range(start, end):
        element = nested_list[i]

        if isinstance(element, list):
            map_to_nested_list(element, map_function)

        else:
            nested_list[i] = map_function(nested_list, i, end)

def add_subsequent_numbers(nested_list: list[int], start: int, end: int):
    # In lexiconizer, this would compare the word at nested_list[start] to the words between
    # nested_list[start+1:end], and add neighbours if appropriate

    element = nested_list[start]

    for i in range(start+1, end):
        # TODO: Check that next element if of compatible type, else will crash
        element += nested_list[i]

    return element

def main():
    # nested_list = [
    #     [1,2,3],
    #     [4,5,6],
    #     [7,8,9]
    # ]
    # # Expected:
    # # [6, 5, 3]
    # # [15, 11, 6]
    # # [24, 17, 9]

    nested_list = [
        [
            [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ],
            [
                [7,8,9],
                [4,5,6],
                [1,2,3],
            ],
            [
                [4,5,6],
                [7,8,9],
                [1,2,3]
            ]
        ],
        [
            [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ],
            [
                [7,8,9],
                [4,5,6],
                [1,2,3],
            ],
            [
                [4,5,6],
                [7,8,9],
                [1,2,3]
            ]
        ],
        [
            [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ],
            [
                [7,8,9],
                [4,5,6],
                [1,2,3],
            ],
            [
                [4,5,6],
                [7,8,9],
                [1,2,3]
            ]
        ],
    ]

    map_to_nested_list(nested_list, add_subsequent_numbers)

    for i in nested_list:
        print(i)


if __name__ == '__main__':
    main()
