# Kadens algorithm is used to find the sub array with largest sum
def max_subarray_with_elements(arr):
    max_sum = current_sum = arr[0]
    start = end = temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return arr[start:end+1], max_sum


# 🔽 Get input from user
input_str = input("Enter the array elements separated by spaces: ")

# 🔄 Convert input string to list of integers
arr = list(map(int, input_str.strip().split()))

# ✅ Call the function
subarray, max_sum = max_subarray_with_elements(arr)

# 📢 Display result
print("Maximum Sum Subarray:", subarray)
print("Maximum Sum:", max_sum)
