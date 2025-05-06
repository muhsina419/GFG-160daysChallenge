def getMinDiff(arr, k):
    n = len(arr)
    if n == 1:
        return 0

    arr.sort()
    min_diff = arr[-1] - arr[0]

    for i in range(1, n):
        if arr[i] - k < 0:
            continue

        min_height = min(arr[0] + k, arr[i] - k)
        max_height = max(arr[i - 1] + k, arr[-1] - k)
        min_diff = min(min_diff, max_height - min_height)

    return min_diff


def main():
    # Input array from user
    arr = list(map(int, input("Enter tower heights (space-separated): ").strip().split()))
    
    # Input k value from user
    k = int(input("Enter the value of K: "))

    result = getMinDiff(arr, k)
    print("Minimum difference after modification:", result)


if __name__ == "__main__":
    main()
