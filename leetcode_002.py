"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    up = 0
    if l1.val + l2.val >= 10:
        ret = ListNode(l1.val + l2.val - 10)
        up = 1
    else:
        ret = ListNode(l1.val + l2.val)
    l1 = l1.next
    l2 = l2.next
    k = ret
    if not l1 and not l2 and up:
        ret.next = ListNode(up)
        return ret
    while l1 or l2:
        if l1 and l2:
            if l1.val + l2.val + up >= 10:
                ret.next = ListNode(l1.val + l2.val + up - 10)
                up = 1
            else:
                ret.next = ListNode(l1.val + l2.val + up)
                up = 0
            ret = ret.next
            l1 = l1.next
            l2 = l2.next
        elif l1:
            if l1.val + up >= 10:
                ret.next = ListNode(l1.val + up - 10)
                up = 1
            else:
                ret.next = ListNode(l1.val + up)
                up = 0
            ret = ret.next
            l1 = l1.next
        elif l2:
            if l2.val + up >= 10:
                ret.next = ListNode(l2.val + up - 10)
                up = 1
            else:
                ret.next = ListNode(l2.val + up)
                up = 0
            ret = ret.next
            l2 = l2.next
        else:
            print('why!!!!')
    if up:
        ret.next = ListNode(up)
    return k

# 1562 / 1562 test cases passed. Runtime: 195 ms  84.34 %

"""
一点点感悟: 1、读题一定要细致,遇到leetcode上不知道的结构时,leetcode一般会给出  结构体
"""

if __name__ == "__main__":
    # 插入节点一
    idx = ListNode(2)
    n = idx
    idx.next = ListNode(4)
    idx = idx.next
    idx.next = ListNode(3)
    # 可以自己写一个 insert 方法 但是只是为了测试可以不用
    # 插入节点二
    idx_1 = ListNode(5)
    n_1 = idx_1
    idx_1.next = ListNode(6)
    idx_1 = idx_1.next
    idx_1.next = ListNode(4)
    # 测试方法正确性
    addTwoNumbers(n, n_1)