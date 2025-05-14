def add_binary_strings(s1, s2):
    # Make both strings the same length by padding with zeros on the left
    max_len = max(len(s1), len(s2))
    s1 = s1.zfill(max_len)
    s2 = s2.zfill(max_len)

    print(f"Padded s1: {s1}")
    print(f"Padded s2: {s2}")

    result = []
    carry = 0

    # Iterate from the end (rightmost bits) to the beginning
    for i in range(max_len - 1, -1, -1):
        bit1 = int(s1[i])
        bit2 = int(s2[i])
        bit_sum = carry + bit1 + bit2

        result_bit = bit_sum % 2
        carry = bit_sum // 2

        result.append(str(result_bit))

        print(f"Index {i} -> s1[{i}]={bit1}, s2[{i}]={bit2}, carry={carry}, result_bit={result_bit}")

    # If there's a carry left, add it to the front
    if carry:
        result.append('1')
        print(f"Final carry added: 1")

    # The result is built backwards, so reverse it
    result.reverse()
    final_result = ''.join(result).lstrip('0') or '0'

    print(f"Final binary result (no leading zeros): {final_result}")
    return final_result

# Example usage
if __name__ == "__main__":
    s1 = "1101"
    s2 = "111"
    print(f"Sum of {s1} and {s2} is: {add_binary_strings(s1, s2)}")
