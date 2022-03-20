def linearSearch():
    array = [2, 4, 0, 1, 9]
    x = 1
    n = len(array)
    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

result = linearSearch()

if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)


 