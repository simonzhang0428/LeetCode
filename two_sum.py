# 06/22/2020

# 1. Two Sum
# Easy 15316/555 => like/dislike

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def twoSum(nums, target):
    """
    >>> print(twoSum([2, 7, 11, 15], 13))
    [0, 2]
    """
    result = {}
    for i, num in enumerate(nums):
        remain = target - num
        if remain not in result:
            result[num] = i
        else:
            return [result[remain], i]


if __name__ == '__main__':
    import doctest

    doctest.testmod()

"""
% python3 two_sum.py -v

Trying:
    nums = [2, 7, 11, 15]
Expecting nothing
ok
Trying:
    target = 9
Expecting nothing
ok
Trying:
    lst = twoSum(nums, target)
Expecting nothing
ok
Trying:
    print(lst)
Expecting:
    [0, 1]
ok
1 items had no tests:
    __main__
1 items passed all tests:
   4 tests in __main__.twoSum
4 tests in 2 items.
4 passed and 0 failed.
Test passed.
"""