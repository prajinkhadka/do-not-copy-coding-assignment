def binarySearch_my_new_func(array, x, low, high):
    array = [3, 4, 5, 6, 7, 8, 9]
    x = 4
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
result_my_new_var = binarySearch_my_new_func()
if result_my_new_var != -1:
    print('Element is present at index ' + str(result_my_new_var))
else:
    print('Not found')