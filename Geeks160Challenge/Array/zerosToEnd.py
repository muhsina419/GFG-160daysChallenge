def PushZerosToEnd(arr):
    n = len(arr)
    count = 0  # Position to place the next non-zero element

    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1

    return arr

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    result = PushZerosToEnd(arr)
    print("Array after pushing zeros to end:", result)
