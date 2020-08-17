# 344. Reverse String
# Easy

# Write a function that reverses a string. The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
#
#
# Example 1:
#
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
#
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.

    >>> s = ["h","e","l","l","o"]
    >>> reverseString(s)
    >>> print(s)
    ['o', 'l', 'l', 'e', 'h']
    """
    # s.reverse()
    if len(s) <= 1:
        return

    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1