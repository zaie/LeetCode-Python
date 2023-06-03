# 由于只能一步步地走，人移动的范围必然是一段连续的区间。

# 如果反复左右移动，会白白浪费移动次数，所以最优方案要么先向右再向左，要么先向左再向右（或者向一个方向走到底）。

# 设向左走最远可以到达 fruits[left][0]\textit{fruits}[\textit{left}][0]fruits[left][0]，这可以用枚举或者二分查找得出，其中 left\textit{left}left 是最小的满足

# fruits[left][0]≥startPos−k 
# 的下标。

# 假设位置不超过 startPos 的最近水果在 fruits[right][0]，那么当 right 增加时，left 不可能减少，有单调性，因此可以用同向双指针（滑动窗口）解决。不了解的同学可以先看上面的视频讲解。

# 如何判断 left 是否需要增加呢？

# 如果先向右再向左，那么移动距离为

# (fruits[right][0]−startPos)+(fruits[right][0]−fruits[left][0]) 
# 如果先向左再向右，那么移动距离为

# (startPos−fruits[left][0])+(fruits[right][0]−fruits[left][0])
# 如果上面两个式子均大于 k，就说明 fruits[left][0] 太远了，需要增加 left。

# 对于 right，它必须小于 n，且满足

# fruits[right][0]≤startPos+k
# 移动 left 和 right 的同时，维护窗口内的水果数量 s，同时用 s 更新答案的最大值。

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = bisect_left(fruits, [startPos - k])  # 向左最远能到 fruits[left][0]
        right = bisect_left(fruits, [startPos + 1])  # startPos 右边最近水果（因为下面求的是左闭右开区间）
        ans = s = sum(c for _, c in fruits[left:right])  # 从 fruits[left][0] 到 startPos 的水果数
        while right < len(fruits) and fruits[right][0] <= startPos + k:
            s += fruits[right][1]  # 枚举最右位置为 fruits[right][0]
            while fruits[right][0] * 2 - fruits[left][0] - startPos > k and \
                  fruits[right][0] - fruits[left][0] * 2 + startPos > k:
                s -= fruits[left][1]  # fruits[left][0] 无法到达
                left += 1
            ans = max(ans, s)  # 更新答案最大值
            right += 1  # 继续枚举下一个最右位置
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-fruits-harvested-after-at-most-k-steps/solutions/2254860/hua-dong-chuang-kou-jian-ji-xie-fa-pytho-1c2d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
