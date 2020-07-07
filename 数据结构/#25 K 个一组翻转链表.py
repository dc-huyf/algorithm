# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
# 多好的题目，顺便复习一下反转链表>_<
本质上就是翻转链表+递归
'''
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 考虑特殊情形
        if head == None:
            return head
        a, b = head, head
        for i in range(k-1): # 若节点数不满k个，则直接返回head;若满足，则找出第K个节点为b
            if b == None:
                return head
            b = b.next
        # 先翻转前k个节点，然后递归
        new_head =  self.reverse(a, b)
        # 此时a为末尾节点
        a.next = self.reverseKGroup(b, k)
        return new_head

    # 写给定链表头部，写一个反转链表
    def reverse(self, head, b):
        pre = None
        while head != b:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre








