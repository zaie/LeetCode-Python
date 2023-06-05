首先 pre 指针指向 Null，cur 指针指向 head；

当 cur != Null，执行循环。
    先将 cur.next 保存在 temp 中防止链表丢失：temp = cur.next
    接着把 cur.next 指向前驱节点 pre：cur.next = pre
    然后将 pre 往后移一位也就是移到当前 cur 的位置：pre = cur
    最后把 cur 也往后移一位也就是 temp 的位置：cur = temp

当 cur == Null，结束循环，返回 pre。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            temp = cur.next   # 先把原来cur.next位置存起来
            cur.next = pre
            pre = cur
            cur = temp
        return pre

# 作者：憨憨阿狗
# 链接：https://leetcode.cn/problems/reverse-linked-list/solutions/305898/tu-jie-liu-cheng-python3die-dai-xiang-jie-by-han-h/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

