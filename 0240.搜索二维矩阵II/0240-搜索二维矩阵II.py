体思路是尽可能多的排除掉无关 行/列 ，可以从 第一排最后一个/第一列最后一个 开始搜索，这里选择从 第一排最后一个 开始
由于行列规则等价，搜索策略 先按行排除/按列排除 也是等价的，这里选择 按行排除
搜索规则：小于 target 则向左搜索，大于 则向下搜索，可以保证 global search
若超出 矩阵大小 则意味着没有匹配 target，输出 False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col - 1
        while matrix[i][j] != target:
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
            if i >= row or j < 0:
                return False
        return True

作者：Eloise
链接：https://leetcode.cn/problems/search-a-2d-matrix-ii/solutions/618999/si-lu-qing-xi-zhe-xian-sou-suo-by-eloise-kisj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
