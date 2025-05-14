class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        result = 0
        n = len(s)

        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Check for sign
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        # Convert digits to integer
        while i < n and s[i].isdigit():
            result = result * 10 + (ord(s[i]) - ord('0'))
            i += 1

        result *= sign

        # Clamp to 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("   -42"))            # Output: -42
    print(sol.myAtoi("4193 with words"))   # Output: 4193
    print(sol.myAtoi("words and 987"))     # Output: 0
    print(sol.myAtoi("-91283472332"))      # Output: -2147483648
