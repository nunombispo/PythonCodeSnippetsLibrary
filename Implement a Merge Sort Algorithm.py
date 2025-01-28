def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


# Example usage
unsorted_list = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(unsorted_list))  # Output: [3, 9, 10, 27, 38, 43, 82]

# Why?
# Merge Sort is a stable, divide-and-conquer sorting algorithm with a guaranteed O(n log n) time complexity.
# This snippet demonstrates splitting, recursive sorting, and merging, making it a cornerstone algorithm for
#     mastering sorting techniques.
