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

# 方法三：双指针
# 动态规划的做法中，需要维护两个数组 leftMax 和 rightMax，因此空间复杂度是 O(n)O(n)O(n)。是否可以将空间复杂度降到 O(1)O(1)O(1)？
# 注意到下标 i 处能接的雨水量由 leftMax[i] 和 rightMax[i] 中的最小值决定。由于数组 leftMax 是从左往右计算，数组 rightMax 是从右往左计算，因此可以使用双指针和两个变量代替两个数组。
# 维护两个指针 left 和 right，以及两个变量 leftMax 和 rightMax，初始时 left=0,right=n−1,leftMax=0,rightMax=0。
# 指针 left 只会向右移动，指针 right 只会向左移动，在移动指针的过程中维护两个变量 leftMax 和 rightMax 的值。

# 当两个指针没有相遇时，进行如下操作：
# 使用 height[left] 和 height[right] 的值更新 leftMax 和 rightMax 的值；
# 如果 height[left]<height[right]，则必有 leftMax<rightMax，下标 left 处能接的雨水量等于 leftMax−height[left]，将下标 left 处能接的雨水量加到能接的雨水总量，然后将 left 加 1（即向右移动一位）；
# 如果 height[left]≥height[right]，则必有 leftMax≥rightMax，下标 right 处能接的雨水量等于 rightMax−height[right]，将下标 right 处能接的雨水量加到能接的雨水总量，然后将 right 减 1（即向左移动一位）。
# 当两个指针相遇时，即可得到能接的雨水总量。

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        
        return ans
# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/trapping-rain-water/solutions/692342/jie-yu-shui-by-leetcode-solution-tuvc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
