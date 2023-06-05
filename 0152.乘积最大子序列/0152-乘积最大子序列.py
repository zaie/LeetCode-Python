思路一：类似滑动窗口的感觉

product(i, j) = product(0, j) / product(0, i) 从数组 i 到 j 的累乘等于 从数组开头到 j 的累乘除以从数组开头到 i 的累乘(这里先忽略 0 的情况)，要考虑三种情况

累乘的乘积等于 0，就要重新开始

累乘的乘积小于 0，要找到前面最大的负数，这样才能保住从 i 到 j 最大

累乘的乘积大于 0，要找到前面最小的正数，同理！

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        # 目前的累乘
        cur_pro = 1
        # 前面最小的正数
        min_pos = 1
        # 前面最大的负数
        max_neg = float("-inf")
        # 结果
        res = float("-inf")
        for num in nums:
            cur_pro *= num
            # 考虑三种情况
            # 大于0
            if cur_pro > 0:
                res = max(res, cur_pro // min_pos)
                min_pos = min(min_pos, cur_pro)
            # 小于0
            elif cur_pro < 0:
                if max_neg != float("-inf"):
                    res = max(res, cur_pro // max_neg)
                else:
                    res = max(res, num)
                max_neg = max(max_neg, cur_pro)
            # 等于0 
            else:
                cur_pro = 1
                min_pos = 1
                max_neg = float("-inf")
                res = max(res, num)
        return res 

作者：powcai
链接：https://leetcode.cn/problems/maximum-product-subarray/solutions/17709/duo-chong-si-lu-qiu-jie-by-powcai-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
