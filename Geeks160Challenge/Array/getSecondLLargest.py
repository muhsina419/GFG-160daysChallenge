def getSecondLargest(arr):
    n=len(arr)
    if n<2:
            return -1
    largest=second=-1
    for i in range (n):
        if arr[i] > largest :
                second = largest
                largest = arr[i]
        elif arr[i] > second and arr[i] != largest:
                second = arr [i]
    return second

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    
    result = getSecondLargest(arr)
    
    print("Second largest element is:", result)