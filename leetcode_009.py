"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    flag = 1 if x > 0 else -1
    # 如果要求范围在32位整数,就用下边那句
    # return int(repr(flag * x)[::-1]) == x if -2 ** 31 <= x <= 2 ** 31 - 1 else False
    return int(repr(flag * x)[::-1]) == x

# 11507 / 11507 test cases passed.  Runtime: 532 ms 99.52 %


if __name__ == "__main__":
    print(isPalindrome(1234321))
