"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    ret = ''.join(reversed(str(abs(x))))
    ret = int(ret) if x > 0 else -int(ret)
    if - pow(2, 31) < ret < pow(2, 31) - 1:
        return ret
    return 0
    # return ret if - pow(2, 31) < ret < pow(2, 31) - 1 else 0

# 1032 / 1032 test cases passed. Runtime: 98 ms 50%


# def reverse(x):
#     """
#     :type x: int
#     :rtype: int
#     """
#     n = 0
#     flag = 1 if x > 0 else -1
#     x = abs(x)
#     while x:
#         y = x % 10
#         n = n * 10 + y
#         x //= 10
#     return n * flag if - pow(2, 31) < n * flag < pow(2, 31) - 1 else 0

# 1032 / 1032 test cases passed. Runtime: 98 ms 59%


# def reverse(x):
#     """
#     :type x: int
#     :rtype: int
#     """
#     flag = 1 if x > 0 else -1
#     ret = int(repr(flag * x)[::-1])
#     return ret * flag if -2 ** 31 <= ret <= 2 ** 31 - 1 else 0

# 1032 / 1032 test cases passed. Runtime: 89 ms  98.57 %

"""
一点点感悟: 1、在python中 数值型字符串  与 数值 是等价的
           2、善用字符串的方法、三元表达式、与强转可以精简代码,但性能有所损失
           3、整除时应使用  地板除
           4、python内置函数的性能是C级别的, 所以能用内置方法尽量用内置方法
           5、切片性能是C级别的,能用切片尽量使用切片
           6、利用小技巧 负负得正  正成正 仍然为正
"""

if __name__ == "__main__":
    testcase = [-123, 321, 120, 1534236469]
    for case in testcase:
        print(reverse(case))
