# Pattern Matching in a Text
# This script finds all starting indices where a pattern string appears in a text string

def find_pattern_indices(txt, pat):
    # List to store result indices
    result = []

    # Lengths of the text and pattern
    n = len(txt)
    m = len(pat)

    # Loop over the text with a sliding window of length equal to the pattern
    for i in range(n - m + 1):
        # Check if the current substring matches the pattern
        if txt[i:i + m] == pat:
            result.append(i)  # If match found, add index to result list

    return result


# -------------------- #
# Example: Test Case
# -------------------- #

if __name__ == "__main__":
    # Input strings
    txt = "abcaabbb"
    pat = "ab"

    # Find all occurrences
    indices = find_pattern_indices(txt, pat)

    # Output the result
    print("Pattern found at indices:", indices)
