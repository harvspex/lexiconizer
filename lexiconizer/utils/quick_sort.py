def quick_sort(lexicon):
    def swap(lst, idx_a, idx_b):
        lst[idx_a], lst[idx_b] = lst[idx_b], lst[idx_a]
      
    def quick_sort_inner(lexicon, left=None, right=None):
        if left is None and right is None:
            left = 0
            right = len(lexicon) - 1
        if left < right:
            pivot = partition(lexicon, left, right)
            quick_sort_inner(lexicon, left, pivot-1)
            quick_sort_inner(lexicon, pivot+1, right)

    def partition(sub_list, left, right):
        mid = (left + right) // 2
        pivot = sub_list[mid]
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

    quick_sort_inner(lexicon)