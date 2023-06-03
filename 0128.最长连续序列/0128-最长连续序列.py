class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = {}
        res = 0
        for num in nums:
            if num not in lookup:
                # 判断左右是否可以连起来
                left = lookup[num - 1] if num - 1 in lookup else 0
                right = lookup[num + 1] if num + 1 in lookup else 0
                # 记录长度
                lookup[num] = left + right + 1
                # 把头尾都设置为最长长度
                lookup[num - left] = left + right + 1
                lookup[num + right] = left + right + 1
                res = max(res, left + right + 1)
        return res

# 作者：powcai
# 链接：https://leetcode.cn/problems/longest-consecutive-sequence/solutions/14152/ji-he-huo-zhe-ha-xi-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
