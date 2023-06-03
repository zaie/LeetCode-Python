# 回溯算法 + dfs
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def core_function(i, j, k, visited):
            #print(i,j, k,visited)
            if k == len(word):
                return True
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited \
                and board[tmp_i][tmp_j] == word[k]: # 如果位置合法，没有被访问过，词内容也正确
                    visited.add((tmp_i, tmp_j))
                    if core_function(tmp_i, tmp_j, k+1, visited):
                        return True
                    visited.remove((tmp_i, tmp_j)) # 回溯
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and core_function(i, j, 1,{(i, j)}) :
                        return True
        return False

作者：powcai
链接：https://leetcode.cn/problems/word-search/solutions/6907/hui-su-dfs-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
