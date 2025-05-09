#To find the maximum sum of circular sub array starting from last element
def circularSubarraySum(arr):
    if not arr:
        return -2147483648  # Return INT_MIN for empty array, as per GFG

    total_sum = sum(arr)  # sum of all elements in the array
    cur_max = max_sum = arr[0]
    cur_min = min_sum = arr[0]

    for i in range(1, len(arr)):  # Starting from the second element
        num = arr[i]

        # Kadane for max subarray
        cur_max = max(num, cur_max + num)
        max_sum = max(max_sum, cur_max)

        # Kadane for min subarray
        cur_min = min(num, cur_min + num)
        min_sum = min(min_sum, cur_min)

    # If all numbers are negative, return the max (don't wrap)
    if total_sum == min_sum:
        return max_sum

    # Else, return the better of circular and non-circular max
    return max(max_sum, total_sum - min_sum)


# Taking user input for the array
if __name__ == "__main__":
    # Input: Prompt the user to enter a space-separated list of integers
    user_input = input("Enter the array elements (space-separated): ")
    
    # Convert the input string to a list of integers
    arr = list(map(int, user_input.split()))

    # Call the function and print the result
    result = circularSubarraySum(arr)
    print(f"The maximum circular subarray sum is: {result}")
