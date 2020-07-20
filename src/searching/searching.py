# TO-DO: implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # check to see if the end is greater than the start,
    # to see if there is anything between the start and the end
    if end >= start:
        # create the middle by adding the start and the end and dividing by // (floor division --> results in a whole number)
        mid = (start+end)//2
        # check to see if the mid point (index) is equal to the target
        if arr[mid] == target:
            # if so, return the mid point
            return mid
        # if the mid point is greater than the target,
        elif arr[mid] > target:
            # decrement the mid point by 1 and recursively call
            # the function again passing the new mid point
            # as the end
            return binary_search(arr, target, start, mid-1)
        # if the mid point is less than the target,
        else:
            # increment the mid point by 1 and recursively call
            # the function again passing the new mid point
            # as the start
            return binary_search(arr, target, mid+1, end)
    # if the start is the same or larger than the end,
    # return false (-1)
    else: return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is 
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass