# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        1. 比较朴素的思路：
        遍历一遍A、B,确定链表长度。若A比B长n，则A先走n步; 代码又臭又长
        '''
        len1 = 0
        len2 = 0
        h1 = headA
        h2 = headB
        while h1 != None:
            h1 = h1.next
            len1 += 1
        while h2 != None:
            h2 = h2.next
            len2 += 1
        diff = abs(len1 - len2)
        if len1 > len2:
            while diff > 0:
                headA = headA.next
                diff -= 1
        else:
            while diff > 0:
                headB = headB.next
                diff -= 1
        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return headB


class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        2. 比较fancy的想法：假设A ------*### B ...*###
        拼在一起：
                ------*###...*### AB
                ...*###------*### BA
        '''
        h1, h2 = headA, headB
        while h1 != h2:
            h1 = h1.next if h1 else headB
            h2 = h2.next if h2 else headA
        return h1



