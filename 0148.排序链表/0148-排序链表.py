# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #1. 一分为二
        #2. 各自排序
        #3. 合二为一
        
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
            
        first = head
        second = pre.next
        pre.next = None
        # print first.val, second.val
        sortedfirst = self.sortList(first)
        sortedsecond = self.sortList(second)
        
        return self.merge(sortedfirst, sortedsecond)
        
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            tmp = ListNode(l1.val)
            tmp.next = self.merge(l1.next, l2)
        else:
            tmp = ListNode(l2.val)
            tmp.next = self.merge(l1, l2.next)
            
        return tmp
    
# 应该和上面的思路相同
        #1. 一分为二
        #2. 各自排序
        #3. 合二为一
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head
        slow = head
        fast = head
        # 用快慢指针分成两部分
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 找到左右部分, 把左部分最后置空
        mid = slow.next
        slow.next = None
        # 递归下去
        left = self.sortList(head)
        right = self.sortList(mid)
        # 合并
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        p = dummy
        l = left
        r = right

        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
                p = p.next
            else:
                p.next = r
                r = r.next
                p = p.next
        if l:
            p.next = l
        if r:
            p.next = r
        return dummy.next

作者：Junhao
链接：https://leetcode.cn/problems/sort-list/solutions/215640/lc148-jian-ji-pythongui-bing-shi-xian-by-jhhuang/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
