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
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = {}
    for i, num in enumerate(nums):
        remain = target - num
        if remain not in result:
            result[num] = i
        else:
            return [result[remain], i]
