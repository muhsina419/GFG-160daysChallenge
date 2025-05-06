class Solution:
    # Function to find maximum product subarray
    def maxProduct(self, arr):
        if not arr:
            return 0

        max_end_here = min_end_here = max_so_far = arr[0]

        for num in arr[1:]:
            if num == 0:
                max_end_here = min_end_here = 0
                max_so_far = max(max_so_far, 0)
                continue

            temp_max = max_end_here
            max_end_here = max(num, num * max_end_here, num * min_end_here)
            min_end_here = min(num, num * temp_max, num * min_end_here)

            max_so_far = max(max_so_far, max_end_here)

        return max_so_far

# Input from the user
if __name__ == "__main__":
    # Take input like: -2 6 -3 -10 0 2
    user_input = input("Enter the array elements separated by spaces: ")
    
    # Convert to list of integers
    arr = list(map(int, user_input.strip().split()))

    sol = Solution()
    result = sol.maxProduct(arr)
    print("Maximum product subarray is:", result)
