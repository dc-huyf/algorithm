# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 暴力解法
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        res = None
        for list in lists:
            res = self.combineTwoLists(list, res)
        return res

    def combineTwoLists(self, list1: ListNode, list2: ListNode):
        res = p = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                p.next = list2
                list2 = list2.next
            else:
                p.next = list1
                list1 = list1.next
            p = p.next

        p.next = list1 if not list2 else list2
        return res.next

import heapq
class Solution2:
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        # 富比较方法，学到了
        def __lt__(self,other):
            return self.val < other.val
        ListNode.__lt__ = __lt__

        if len(lists) == 0:
            return None
        res = p = ListNode()
        # 头节点加入到队列中
        pq = []
        for l in lists:
            if l:
                heapq.heappush(pq, l)
        while pq:
            tmp = heapq.heappop(pq)
            p.next = tmp
            p = p.next
            tmp = tmp.next
            if tmp:
                heapq.heappush(pq, tmp)
        return res.next