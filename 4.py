arr = [2, 4, 5, 6, 8, 9, 11, 56]


def binarySearch(target, data, low, high):
    if low > high:
        return True
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return f"Your data is on index {mid} and value is {data[mid]} "
        elif target < data[mid]:
            return binarySearch(target, data, low, mid - 1)
        else:
            return binarySearch(target, data, mid + 1, high)


print(binarySearch(5, arr, 0, len(arr)))
