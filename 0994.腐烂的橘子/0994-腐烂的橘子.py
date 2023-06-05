1. 首先分别将腐烂的橘子和新鲜的橘子保存在两个集合中；
2. 模拟广度优先搜索的过程，方法是判断在每个腐烂橘子的四个方向上是否有新鲜橘子，如果有就腐烂它。
每腐烂一次时间加 1，并剔除新鲜集合里腐烂的橘子；
3. 当橘子全部腐烂时结束循环。

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2} # 腐烂集合
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}  # 新鲜集合
        time = 0
        while fresh:
            if not rotten: return -1
            rotten = {(i + di, j + dj) for i, j in rotten for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)] if (i + di, j + dj) in fresh} # 即将腐烂的如果在新鲜的集合中，就将它腐烂
            fresh -= rotten # 剔除腐烂的
            time += 1
        return time

作者：z1m
链接：https://leetcode.cn/problems/rotting-oranges/solution/yan-du-you-xian-sou-suo-python3-c-by-z1m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
