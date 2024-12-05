def quick_sort(word_list: list[str]) -> list[str]:
    """
    Sorts a list of strings using the Quick Sort algorithm.

    Args:
        word_list (list[str]): The list of strings to sort.

    Returns:
        list[str]: The sorted list of strings.
    """
    def swap(lst: list, idx_a: int, idx_b: int):
        """
        Swaps two elements in a list.

        Args:
            lst (list): The list containing elements to swap.
            idx_a (int): Index of the first element.
            idx_b (int): Index of the second element.
        """
        lst[idx_a], lst[idx_b] = lst[idx_b], lst[idx_a]

    def quick_sort_inner(word_list: list[str], left: int=None, right: int=None):
        """
        Recursively sorts a sublist using Quick Sort.

        Args:
            word_list (list[str]): The list of strings to sort.
            left (int, optional): The starting index of the sublist
                (Default: None, meaning 0).
            right (int, optional): The ending index of the sublist
                (Default: None, meaning the length of `word_list` - 1).
        """
        if left is None and right is None:
            left = 0
            right = len(word_list) - 1
        if left < right:
            pivot: int = partition(word_list, left, right)
            quick_sort_inner(word_list, left, pivot-1)
            quick_sort_inner(word_list, pivot+1, right)

    def partition(sub_list: list[str], left: int, right: int) -> int:
        """
        Partitions a sublist around a pivot for Quick Sort.

        Args:
            sub_list (list[str]): The list to partition.
            left (int): The starting index of the sublist.
            right (int): The ending index of the sublist.

        Returns:
            int: The index of the pivot after partitioning.
        """
        mid: int = (left + right) // 2
        pivot: int = sub_list[mid]
        swap(sub_list, mid, right)

        while left < right:
            while left < right and sub_list[left] <= pivot:
                left += 1
            if left < right:
                swap(sub_list, left, right)
                right -= 1
            while right > left and sub_list[right] >= pivot:
                right -= 1
            if right > left:
                swap(sub_list, left, right)
                left += 1
        return left

    quick_sort_inner(word_list)

    return word_list