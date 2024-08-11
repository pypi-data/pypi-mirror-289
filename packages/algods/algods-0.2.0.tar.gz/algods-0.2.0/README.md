# Algods
**Algods** is a Python package designed to help programmers save time by providing efficient implementations of common algorithms and data structures. 

This module includes well-known search algorithms and is ideal for those looking to quickly implement these algorithms in their projects.

# Contents
- ## Algorithms
    - Linear Search
    - Binary Search
    - Jump Search
    - Interpolation Search

# Installation
Installing Algods is straightforward. Simply open a terminal and run:

```bash
pip install algods
```

# Compatibility
Algods is compatible with Python 3.8 and above.

# Documentation:
Enough talk. Let's come to the main part. Documentation. Here is a detailed breakdown of all the functions. 

## linear_search(arr: List[int], target: int) -> Union[int, None]
This function takes a list of integers (`arr`), which can be either unsorted or sorted, and a target integer (`target`) as inputs. It iterates through each element in the list, comparing it to the target. If a match is found, the function returns the index of the matching element. If the target is not found in the list, the function returns `None`.

## binary_search(arr: List[int], target: int) -> Union[int, None]
This function takes a sorted list of integers (`arr`) and a target integer (`target`) as inputs. It repeatedly divides the list in half and compares the middle element to the target until a match is found or the list cannot be divided further. If a match is found, the function returns the index of the matching element. If the target is not found, the function returns `None`.

## jump_search(arr: List[int], target: int) -> Union[int, None]
This function performs a jump search on a sorted list of integers (`arr`) to find a target integer (`target`). The jump search algorithm divides the list into blocks of fixed size and performs a linear search within the identified block where the target might be located. The steps are as follows:

- **Determine Block Size**: Calculate the block size as the square root of the length of the list.
- **Jump Through Blocks**: Start from the beginning of the list and jump ahead by the block size until you reach a block where the target could be located.
- **Linear Search in Block**: Once the correct block is identified, perform a linear search within that block to find the exact position of the target.

If the target is found, the function returns the index of the target. If the target is not present in the list, the function returns `None`.

## interpolation_search(arr: List[int], target: int) -> Union[int, None]
This function performs an interpolation search on a sorted list of integers (`arr`) to find a target integer (`target`). The interpolation search algorithm estimates the position of the target based on the values in the list, assuming a uniform distribution. The steps are as follows:

- **Estimate Position**: The algorithm calculates a probable position for the target using the formula:
```
                (target - arr[low])×(high - low)
    pos = low+ _________________________________
                      arr[high] - arr[low]
```
where `low` and `high` are the indices representing the current search range in the list.
- **Check Estimated Position**: The algorithm compares the value at the estimated position with the target:
     - If it matches, the function returns the index of the target.
     - If the target is less than the value at the estimated position, the search continues in the lower subarray.
     - If the target is greater, the search continues in the upper subarray.
- **Repeat or Return**: The process is repeated, adjusting the search range based on the estimated position, until the target is found or the search range is exhausted.

If the target is found, the function returns its index. If the target is not present in the list, the function returns `None`.

# Usage
Here, I will show you how to import the algorithms and use them.

```python
from algods.search import binary_search

array = [1, 3, 5, 6]
target = 6

result = binary_search(array, target)
print(result)
```

# Contributing
We welcome contributions to Algods! If you'd like to contribute, please refer to our **[CONTRIBUTING.md](https://github.com/UniquePython/Algods/blob/main/CONTRIBUTING.md)** for guidelines on how to get started.

Your contributions help us improve and expand the functionality of Algods.