# 设「第一个公共节点」为 node ，「链表 headA」的节点数量为 a ，「链表 headB」的节点数量为 b ，「两链表的公共尾部」的节点数量为 c ，则有：
# 头节点 headA 到 node 前，共有 a−c 个节点；
# 头节点 headB 到 node 前，共有 b−c 个节点；


# 考虑构建两个节点指针 A , B 分别指向两链表头节点 headA , headB ，做如下操作：

# 指针 A 先遍历完链表 headA ，再开始遍历链表 headB ，当走到 node 时，共走步数为：
# a+(b−c)

# 指针 B 先遍历完链表 headB ，再开始遍历链表 headA ，当走到 node 时，共走步数为：
# b+(a−c)
# 因为 a+(b−c) = b+(a−c)，即此时指针 A , B 重合，并有两种情况：
#     若两链表 有 公共尾部 (即 c>0) ：指针 A , B 同时指向「第一个公共节点」node 。
#     若两链表 无 公共尾部 (即 c=0) ：指针 A , B 同时指向 null。
#     因此返回 A 即可。

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B: # 就算没有公共节点，A , B 同时指向 null也不会导致死循环
            A = A.next if A else headB
            B = B.next if B else headA
        return A

# 作者：Krahets
# 链接：https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/12624/intersection-of-two-linked-lists-shuang-zhi-zhen-l/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
