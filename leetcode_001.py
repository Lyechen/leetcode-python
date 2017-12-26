"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


# slow solution
def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
# Time Limit Exceeded


# Medium solution
# def twoSum(nums, target):
#     if len(nums) <= 1:
#         return False
#     for i in range(len(nums)):
#         if target - nums[i] in nums[i+1:]:
#             return [i, i + nums[i+1:].index(target - nums[i]) + 1]
# 19 / 19 test cases passed  Runtime: 1649 ms   17%


# fast solution
# def twoSum(nums, target):
#     if len(nums) <= 1:
#         return False
#     _dict = {}
#     for i in range(len(nums)):
#         if nums[i] in _dict:
#             return [_dict[nums[i]], i]
#         else:
#             _dict[target - nums[i]] = i
# 19 / 19 test cases passed. Runtime: 56 ms  82%

"""
一点点感悟: 1、在不得不使用多层循环的时候,可以看看是不是可以用外层变量替代内层循环,这样便能将循环减少一次
              类似于 x + y + z = target    ==>  z = target - x - y 这样便能将 n^3 降到 n^2 左右
           2、字典的索引是 O(1)级别的,可以用字典解决的尽量用字典
"""


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))
