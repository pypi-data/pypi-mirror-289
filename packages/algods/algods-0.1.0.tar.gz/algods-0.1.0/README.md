# Algods
**Algods** is dedicated to help programmers **save** their precious time by providing functions for common algorithms and data structures.

A big challenge that I faced during making this module is that I did **NOT** know anything about algorithms or data structures. I had to spend hours and hours on different online courses to write this module. 

Currently, this module features only 2 *search* algorithms - **linear search** and **binary search**. In future, I plan to add more categories of algorithms and data structures like *merge*, *sort*, *linked lists*, etc. 

# Installation
Installing Algods is pretty simple and intuitive.

- On Linux, run:
```terminal
sudo pip install algods
```

- On macOS or Windows, run:
```terminal
pip install algods
```

# Documentation:
Enough talk. Let's come to the main part. Documentation. Here is a detailed breakdown of all the functions. Examples are provided for better understanding.

## linear_search(arr: List[int], target: int) -> Union[int, None]
This function takes an unsorted/sorted list containing integer values and a target for an input. It loops through each element in the list and checks if it is equal to the target. It returns the index of the element if the target exists in the list, else returns false. 

Example:
* **If target exists in list.**
```python
arr = [4, 1, 6, 3, 8]
target = 6

print(linear_search(arr, target))
```
Output:
```terminal
path/to/file> python lin_search.py
2
```

* **If target does not exist in list.**
```python
arr = [4, 1, 6, 3, 8]
target = 9

print(linear_search(arr, target))
```
Output:
```terminal
path/to/file> python lin_search.py
None
```

## binary_search(arr: List[int], target: int) -> Union[int, None]
This function takes an sorted list containing integer values and a target for an input. It keeps slicing the list in half until the list contains only one element or a match is found. It returns the index of the element if the target exists in the list, else returns false. 

Example:
* **If target exists in list.**
```python
arr = [4, 1, 6, 3, 8]
target = 6

print(binary_search(arr, target))
```
Output:
```terminal
path/to/file> python lin_search.py
2
```

* **If target does not exist in list.**
```python
arr = [4, 1, 6, 3, 8]
target = 9

print(binary_search(arr, target))
```
Output:
```terminal
path/to/file> python lin_search.py
None
```

## binary_search_sorted(arr: List[int], target: int) -> Union[int, None]
This function is exactly the same as `binary_search()`. The only difference is that it works with unsorted lists, contrary to `binary_search()`.

# Contributing

For contributing, check out `CONTRIBUTING.md`.