# Program to check whether two strings are anagrams or not

def anagram_check(s1, s2):
    # Check if sorted versions of both strings are equal
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    s1 = input("Enter the first string: ").strip()
    s2 = input("Enter the second string: ").strip()
    if anagram_check(s1, s2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")