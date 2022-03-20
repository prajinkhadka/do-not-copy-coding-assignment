def linearSearch_my_new_func():
    array = [2, 4, 0, 1, 9]
    x = 1
    n = len(array)
    for i in range(0, n):
        if array[i] == x:
            return i
    return -1
result_my_new_var = linearSearch_my_new_func()
if result_my_new_var == -1:
    print('Element not found')
else:
    print('Element found at index: ', result_my_new_var)