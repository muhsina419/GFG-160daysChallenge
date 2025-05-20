class Solution:
    def minChar(self, s):
        n = len(s)
        for i in range(n):
            # Check if the suffix is a palindrome
            if s[i:] == s[i:][::-1]:
                return i
        return n

# Test the function
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_strings = ["abc", "aacecaaa", "abcd", "aaa", "race"]
    
    for s in test_strings:
        print(f"Input: {s} -> Minimum characters to add: {sol.minChar(s)}")
