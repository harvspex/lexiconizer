def quick_sort(word_list: list[str]):

    def swap(lst: list, idx_a: int, idx_b: int):
        lst[idx_a], lst[idx_b] = lst[idx_b], lst[idx_a]

    def quick_sort_inner(word_list: list[str], left: int=None, right: int=None):
        if left is None and right is None:
            left = 0
            right = len(word_list) - 1
        if left < right:
            pivot: int = partition(word_list, left, right)
            quick_sort_inner(word_list, left, pivot-1)
            quick_sort_inner(word_list, pivot+1, right)

    def partition(sub_list: list[str], left: int, right: int) -> int:
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