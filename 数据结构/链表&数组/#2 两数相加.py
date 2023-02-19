# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        不需要重新构造新链表，直接原地修改l1
        """
        p, q = l1, l2 # 初始化指针
        flag = 0
        i = 0
        while p:
            sum_val = 0
            sum_val += p.val
            if q: sum_val += q.val
            if flag == 1: sum_val += 1
            if sum_val >= 10:
                p.val = sum_val - 10
                flag = 1
            else:
                flag = 0
                p.val = sum_val
            if q: q = q.next
            if p.next:
                p = p.next
            elif q:
                # 关键步骤
                p.next = q
                p = p.next
                q = None
            else:
                break
            i += 1

        if flag == 1: # 遍历结束后，仍有需进位的，则
            p.next = ListNode(1)
        return l1

