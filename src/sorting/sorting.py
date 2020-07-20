# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # Your code here
    merged_arr = []
    left_pointer = 0
    right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            merged_arr.append(left[left_pointer])
            left_pointer += 1
        else:
            merged_arr.append(right[right_pointer])
            right_pointer += 1

    merged_arr.extend(left[left_pointer:])
    merged_arr.extend(right[right_pointer:])
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case
    if len(arr) < 2:
        return arr
    else:
        middle = round(len(arr)/2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left,right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass