dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数

所以，

当 word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]；

当 word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。
注意，针对第一行，第一列要单独考虑，
第一行，是 word1 为空变成 word2 最少步数，就是插入操作
第一列，是 word2 为空，需要的最少步数，就是删除操作

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
        #print(dp)      
        return dp[-1][-1]


# class Solution(object):
#     def minDistance(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         #dp[i][j]±íÊ¾word1[:i + 1]ºÍword2[:j + 1]µÄ½â
#         l1, l2 = len(word1), len(word2)
#         dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        
#         for i in range(l1 + 1):
#             dp[i][0] = i
#         for j in range(l2 + 1):
#             dp[0][j] = j
            
#         for i in range(1, l1 + 1):
#             for j in range(1, l2 + 1):
#                 if word1[i - 1] == word2[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
#         return dp[l1][l2]
        
    
