保存头指针，移动当前指针，比较大小，最后将还没遍历完的直接接上

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = ListNode()
        temp = cur # 保存头指针，移动的是cur指针
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 is not None:
            cur.next = l1
        elif l2 is not None:
            cur.next = l2
        return temp.next
