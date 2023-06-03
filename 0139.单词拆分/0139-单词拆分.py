class Solution:
方法一：动态规划

1. 初始化 dp=[False,⋯,False]，长度为 n+1。n 为字符串长度。dp[i] 表示 s 的前 i 位是否可以用 wordDictword 中的单词表示。
2. 初始化 dp[0]=True，空字符可以被表示。
3.遍历字符串的所有子串，遍历开始索引 i，遍历区间 [0,n)：
    遍历结束索引 j，遍历区间 [i+1,n+1)：
        若 dp[i]=True 且 s[i,⋯,j) 在 wordlist 中：dp[j]=True。
        解释：dp[i]=True 说明 s 的前 i 位可以用 wordDict 表示，则 s[i,⋯,j) 出现在 wordDict 中，说明 s 的前 j 位可以表示。
4. 返回 dp[n]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:       
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]

# 作者：吴彦祖
# 链接：https://leetcode.cn/problems/word-break/solutions/50986/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
