# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 特殊情况
        if not head:
            return head
        a1 = p1 = ListNode(-1)
        a2 = p2 = ListNode(-1)
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
                # 必须断开连接
            tmp = head.next
            head.next = None
            head = tmp
        # 如何串联
        p1.next = a2.next
        return a1.next


