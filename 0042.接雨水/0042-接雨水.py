# 动态规划
# 对于下标 ii，下雨后水能到达的最大高度等于下标 ii 两边的最大高度的最小值，下标 ii 处能接的雨水量等于下标 ii 处的水能到达的最大高度减去 \textit{height}[i]height[i]。

# 朴素的做法是对于数组 \textit{height}height 中的每个元素，分别向左和向右扫描并记录左边和右边的最大高度，然后计算每个下标位置能接的雨水量。假设数组 \textit{height}height 的长度为 nn，该做法需要对每个下标位置使用 O(n)O(n) 的时间向两边扫描并得到最大高度，因此总时间复杂度是 O(n^2)O(n 
# 2
#  )。

# 上述做法的时间复杂度较高是因为需要对每个下标位置都向两边扫描。如果已经知道每个位置两边的最大高度，则可以在 O(n)O(n) 的时间内得到能接的雨水总量。使用动态规划的方法，可以在 O(n)O(n) 的时间内预处理得到每个位置两边的最大高度。

# 创建两个长度为 nn 的数组 \textit{leftMax}leftMax 和 \textit{rightMax}rightMax。对于 0 \le i<n0≤i<n，\textit{leftMax}[i]leftMax[i] 表示下标 ii 及其左边的位置中，\textit{height}height 的最大高度，\textit{rightMax}[i]rightMax[i] 表示下标 ii 及其右边的位置中，\textit{height}height 的最大高度。

# 显然，\textit{leftMax}[0]=\textit{height}[0]leftMax[0]=height[0]，\textit{rightMax}[n-1]=\textit{height}[n-1]rightMax[n−1]=height[n−1]。两个数组的其余元素的计算如下：

# 当 1 \le i \le n-11≤i≤n−1 时，\textit{leftMax}[i]=\max(\textit{leftMax}[i-1], \textit{height}[i])leftMax[i]=max(leftMax[i−1],height[i])；

# 当 0 \le i \le n-20≤i≤n−2 时，\textit{rightMax}[i]=\max(\textit{rightMax}[i+1], \textit{height}[i])rightMax[i]=max(rightMax[i+1],height[i])。

# 因此可以正向遍历数组 \textit{height}height 得到数组 \textit{leftMax}leftMax 的每个元素值，反向遍历数组 \textit{height}height 得到数组 \textit{rightMax}rightMax 的每个元素值。

# 在得到数组 \textit{leftMax}leftMax 和 \textit{rightMax}rightMax 的每个元素值之后，对于 0 \le i<n0≤i<n，下标 ii 处能接的雨水量等于 \min(\textit{leftMax}[i],\textit{rightMax}[i])-\textit{height}[i]min(leftMax[i],rightMax[i])−height[i]。遍历每个下标位置即可得到能接的雨水总量。

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode-solution-tuvc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
