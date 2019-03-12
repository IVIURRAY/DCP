"""
Locate the smallest window to be sorted

Given an array of integers that are out of order, determine the bound of the smallest window that must be sorted
in order for the entire array to be sorted.

E.g given [3, 7, 5, 6, 9], you should return (1, 3)
"""


def solution(arr):
    """
    Compare the arr to a sorted array to find differences

    Time: O(n log n) as you need to sort the array
    Space: O(m log n) sort the original array
    """
    sorted_arr = sorted(arr)
    left, right = None, None

    for i in range(len(sorted_arr)):
        if sorted_arr[i] != arr[i] and left is None:
            left = i
        elif sorted_arr[i] != arr[i]:
            right = i

    return left, right


def solution_2(arr):
    """
    Keep track of a local max/min to find when items are out of place

    Time O(n): Two passes over array
    Space O(1): Creating a few int variables, min / max.
    """
    left, right = None, None
    max_seen, min_seen = -1, 10*10
    n = len(arr)

    for i in range(n):
        max_seen = max(max_seen, arr[i])
        if arr[i] < max_seen:
            right = i

    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, arr[i])
        if arr[i] > min_seen:
            left = i

    return left, right


if __name__ == '__main__':
    for f in [solution, solution_2]:
        print(f([3, 7, 5, 6, 9]))
        print(f([1, 2, 3, 4, 5]))
        print(f([5, 4, 3, 2, 1]))
