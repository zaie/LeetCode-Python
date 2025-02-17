注意到下一个排列总是比当前排列要大，除非该排列已经是最大的排列。我们希望找到一种方法，能够找到一个大于当前序列的新序列，且变大的幅度尽可能小。具体地：

我们需要将一个左边的「较小数」与一个右边的「较大数」交换，以能够让当前排列变大，从而得到下一个排列。

同时我们要让这个「较小数」尽量靠右，而「较大数」尽可能小。当交换完成后，「较大数」右边的数需要按照升序重新排列。这样可以在保证新排列大于原来排列的情况下，使变大的幅度尽可能小。

以排列 [4,5,2,6,3,1][4,5,2,6,3,1][4,5,2,6,3,1] 为例：

我们能找到的符合条件的一对「较小数」与「较大数」的组合为 222 与 333，满足「较小数」尽量靠右，而「较大数」尽可能小。

当我们完成交换后排列变为 [4,5,3,6,2,1][4,5,3,6,2,1][4,5,3,6,2,1]，此时我们可以重排「较小数」右边的序列，序列变为 [4,5,3,1,2,6][4,5,3,1,2,6][4,5,3,1,2,6]。

具体地，我们这样描述该算法，对于长度为 nnn 的排列 aaa：

首先从后向前查找第一个顺序对 (i,i+1)(i,i+1)(i,i+1)，满足 a[i]<a[i+1]a[i] < a[i+1]a[i]<a[i+1]。这样「较小数」即为 a[i]a[i]a[i]。此时 [i+1,n)[i+1,n)[i+1,n) 必然是下降序列。

如果找到了顺序对，那么在区间 [i+1,n)[i+1,n)[i+1,n) 中从后向前查找第一个元素 jjj 满足 a[i]<a[j]a[i] < a[j]a[i]<a[j]。这样「较大数」即为 a[j]a[j]a[j]。

交换 a[i]a[i]a[i] 与 a[j]a[j]a[j]，此时可以证明区间 [i+1,n)[i+1,n)[i+1,n) 必为降序。我们可以直接使用双指针反转区间 [i+1,n)[i+1,n)[i+1,n) 使其变为升序，而无需对该区间进行排序。

class Solution:
def nextPermutation(self, nums: List[int]) -> None:
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
