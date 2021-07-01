# Binary search algorithm implementation Recursive Method

def binary_search(arr, low, high, found_value):
    if high >= low:
        mid = (high + low)//2

        if arr[mid] == found_value:
            return mid
        elif arr[mid] < found_value: 
            return binary_search(arr, mid + 1, high, found_value)
        else:
            return binary_search(arr, low, mid - 1, found_value)
    else:
        return -1

arr = ['a','B','c','f']
found_value = str(input("enter="))
result= binary_search(arr, 0 ,len(arr)-1, found_value)

if result != -1:
    print("find!", str(result))
else:
    print("not find")