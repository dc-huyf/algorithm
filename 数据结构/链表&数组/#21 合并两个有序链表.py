# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 定义虚拟头节点
        res = cur = ListNode(-1)
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 =list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        if not list1:
            cur.next = list2
        if not list2:
            cur.next = list1
        return res.next