# 遍历一遍数组，计算每次 到当天为止 的最小股票价格和最大利润。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit

# 作者：腐烂的橘子
# 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solutions/139559/gu-piao-wen-ti-python3-c-by-z1m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
