class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 深拷贝 matrix -> tmp
        tmp = copy.deepcopy(matrix)
        # 根据元素旋转公式，遍历修改原矩阵 matrix 的各元素
        for i in range(n):
            for j in range(n):
                matrix[j][n - 1 - i] = tmp[i][j]

作者：Krahets
链接：https://leetcode.cn/problems/rotate-image/solutions/1228078/48-xuan-zhuan-tu-xiang-fu-zhu-ju-zhen-yu-jobi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
