"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before
    implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const
    char * argument, please click the reload button  to reset your code definition.
"""
import re

# def isNumber(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     s = s.strip(' ')
#     # s = s.rstrip(' ')
#     if not s:
#         return False
#     if 'e' in s:
#         s = s.split('e')
#     elif '.' in s:
#         s = s.split('.')
#         if s[0] == '':
#             s[0] = '0'
#         elif s[-1] == '':
#             s[-1] = '0'
#     cnt = 0
#     for i in s:
#         if not i:
#             continue
#         if ' ' in i:
#             return False
#         j = "".join((lambda x: (x.sort(), x)[1])(list(i)))
#         i = ''.join(j)
#         if '0' <= i[-1] <= '9':
#             cnt += 1
#     return cnt == len(s)


def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.strip(' ')
    pattern = re.compile(r'(([\+-]?\d*\.\d+e[\+-]?\d+)|([\+-]?\d+[\.\d+]e[\+-]?\d+)|([\+-]?\d+\.e[\+-]?\d+)|([\+-]?\d*\.\d+e\d+)|([\+-]?\d*\.\d+)|([\+-]?\d+\.\d*)|([\+-]?\d+e\+\d+)|([\+-]?\d+[e]??\d+)|([\+-]?\d*))')
    ret = pattern.match(s)
    if ret:
        print(ret.group())
        if ret.group():
            return len(ret.group()) == len(s)
        else:
            return False
    else:
        return False

# 1481 / 1481 test cases passed  Runtime: 135 ms   35.11 %  --  70 %

"""
一点点感悟: 1、多个正则条件时不能加上空格
"""


if __name__ == "__main__":
    # "46.e3"   true
    # ".2e81"   true
    # ".e1"     false
    # "6+1"     false
    # "32.e-80123" true
    # "1.38354e+8" true
    # ".703e+4144" true
    # "166e-02767" true
    print(isNumber("46.e3"))
