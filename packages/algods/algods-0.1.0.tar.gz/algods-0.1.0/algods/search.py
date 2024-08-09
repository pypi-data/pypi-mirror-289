#pyalgo/pyalgo/search.py

from typing import List, Union

def linear_search(arr: List[int], target: int) -> Union[int, None]:
    """
    Perform a linear search on the given list.

    arr: List of elements to search through.
    target: The element to search for.
    return: The index of the target if found, else None.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None

def binary_search(arr: List[int], target: int) -> Union[int, None]:
    """
    Perform a binary search on the given sorted list.

    arr: Sorted list of elements to search through.
    target: The element to search for.
    return: The index of the target if found, else None.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

def sorted_binary_search(arr: List[int], target: int) -> Union[int, None]:
    """
    Perform a binary search on the given list after sorting it.

    arr: List of elements to search through.
    target: The element to search for.
    return: The index of the target if found, else None.
    """
    sorted_arr = sorted(arr)  
    left, right = 0, len(sorted_arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if sorted_arr[mid] == target:
            return arr.index(target)  
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
