def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Example usage
unsorted_list = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(unsorted_list))  # Output: [1, 1, 2, 3, 6, 8, 10]

# Why?
# Quick Sort is a classic divide-and-conquer algorithm with an average time complexity of O(n log n).
# This snippet demonstrates the recursive approach to sorting, making it a staple for learning and
# optimizing sorting techniques.
