from math import sqrt
from typing import List, Union

from validation import handle_edge_cases, check_valid_inputs

def linear_search(arr: List[int], target: int) -> Union[int, None]:
    """
    Perform a linear search on the given list.
    """
    check_valid_inputs(arr, target)
    if (edge_case_result := handle_edge_cases(arr, target)) is not None:
        return edge_case_result
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None


def binary_search(arr: List[int], target: int) -> Union[int, None]:
    """
    Perform a binary search on the given sorted list.
    """
    check_valid_inputs(arr, target)
    if (edge_case_result := handle_edge_cases(arr, target)) is not None:
        return edge_case_result
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


def jump_search(arr: List[int], target: int) -> Union[int, None]:
    """
    Perform a jump search on the given sorted list.
    """
    check_valid_inputs(arr, target)
    if (edge_case_result := handle_edge_cases(arr, target)) is not None:
        return edge_case_result
    length = len(arr)
    step = int(sqrt(length))
    prev = 0
    while arr[min(step, length) - 1] < target:
        prev = step
        step += step
        if prev >= length:
            return None  
    for i in range(prev, min(step, length)):
        if arr[i] == target:
            return i 
    return None  


def interpolation_search(arr: List[int], target: int) -> Union[int, None]:
    """
    Perform an interpolation search on the given sorted list.
    """
    check_valid_inputs(arr, target)
    if (edge_case_result := handle_edge_cases(arr, target)) is not None:
        return edge_case_result
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return None                
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1  
        else:
            high = pos - 1  
    return None  
