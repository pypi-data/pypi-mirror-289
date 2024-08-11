def check_valid_inputs(arr, target):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise TypeError("arr must be a list of integers.")
    if not isinstance(target, int):
        raise TypeError("target must be an integer.")
    
def handle_edge_cases(arr, target):
    length = len(arr)
    if length == 0:
        return None 
    if target < arr[0] or target > arr[-1]:
        return None  
