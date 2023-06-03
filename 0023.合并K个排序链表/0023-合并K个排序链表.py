# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 优先级队列
# 时间复杂度：O(n*log(k))O(n∗log(k))
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         from heapq import *
#         pq = []
#         for i in range(len(lists)):
#             if lists[i]:
#                 heappush(pq, (lists[i].val, i))
#                 lists[i] = lists[i].next
            
#         dummy = ListNode(1)
#         p = dummy
#         while pq:
#             val, idx = heappop(pq)
#             p.next = ListNode(val)
#             p = p.next
#             if lists[idx]:
#                 heappush(pq, (lists[idx].val, idx))
#                 lists[idx] = lists[idx].next
#         return dummy.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 分而治之，两两合并
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return 
        n = len(lists)
        return self.merge(lists, 0, n-1)
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    def mergeTwoLists(self,l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# 应该和上面一个相同
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        res = None #设置初始结果为空
        for listi in lists: #逐个遍历 两两合并
            res = self.mergeTwoLists(res, listi)
        return res
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0) #构造虚节点
        move = dummy #设置移动节点等于虚节点
        while l1 and l2: #都不空时
            if l1.val < l2.val:
                move.next = l1 #移动节点指向数小的链表
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2 #连接后续非空链表
        return dummy.next #虚节点仍在开头

# 作者：千想
# 链接：https://leetcode.cn/problems/merge-k-sorted-lists/solutions/1046759/python-23he-bing-kge-sheng-xu-lian-biao-ep54a/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
            
