class Solution:
    # Function to check if two strings are rotations of each other or not.
    def areRotations(self, s1, s2):
        # Check if lengths are equal
        if len(s1) != len(s2):
            return False
        # Concatenate s1 with itself
        combined = s1 + s1
        # Check if s2 is a substring of the combined string
        return s2 in combined

# Test cases
def run_tests():
    test_cases = [
        ("abcd", "cdab", True),
        ("abcd", "acbd", False),
        ("aaaa", "aaaa", True),
        ("a", "a", True),
        ("abc", "ab", False),
        ("abcde", "eabcd", True),
    ]

    sol = Solution()
    for i, (s1, s2, expected) in enumerate(test_cases):
        result = sol.areRotations(s1, s2)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {i+1}: areRotations('{s1}', '{s2}') → {result} | Expected: {expected} → {status}")

# Run the test function
if __name__ == "__main__":
    run_tests()
