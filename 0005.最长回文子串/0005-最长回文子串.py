对于一个子串而言，如果它是回文串，并且长度大于 222，那么将它首尾的两个字母去除之后，它仍然是个回文串。例如对于字符串 “ababa”\textrm{``ababa''}“ababa”，如果我们已经知道 “bab”\textrm{``bab''}“bab” 是回文串，那么 “ababa”\textrm{``ababa''}“ababa” 一定是回文串，这是因为它的首尾两个字母都是 “a”\textrm{``a''}“a”。

根据这样的思路，我们就可以用动态规划的方法解决本题。我们用 P(i,j)P(i,j)P(i,j) 表示字符串 sss 的第 iii 到 jjj 个字母组成的串（下文表示成 s[i:j]s[i:j]s[i:j]）是否为回文串：

P(i,j)={true,如果子串 Si…Sj 是回文串false,其它情况 P(i,j) = \begin{cases} \text{true,} &\quad\text{如果子串~} S_i \dots S_j \text{~是回文串}\\ \text{false,} &\quad\text{其它情况} \end{cases}
P(i,j)={ 
true,
false,
​
  
如果子串 S 
i
​
 …S 
j
​
  是回文串
其它情况
​
 
这里的「其它情况」包含两种可能性：

s[i,j]s[i, j]s[i,j] 本身不是一个回文串；

i>ji > ji>j，此时 s[i,j]s[i, j]s[i,j] 本身不合法。

那么我们就可以写出动态规划的状态转移方程：

P(i,j)=P(i+1,j−1)∧(Si==Sj) P(i, j) = P(i+1, j-1) \wedge (S_i == S_j)
P(i,j)=P(i+1,j−1)∧(S 
i
​
 ==S 
j
​
 )
也就是说，只有 s[i+1:j−1]s[i+1:j-1]s[i+1:j−1] 是回文串，并且 sss 的第 iii 和 jjj 个字母相同时，s[i:j]s[i:j]s[i:j] 才会是回文串。

上文的所有讨论是建立在子串长度大于 222 的前提之上的，我们还需要考虑动态规划中的边界条件，即子串的长度为 111 或 222。对于长度为 111 的子串，它显然是个回文串；对于长度为 222 的子串，只要它的两个字母相同，它就是一个回文串。因此我们就可以写出动态规划的边界条件：

{P(i,i)=trueP(i,i+1)=(Si==Si+1) \begin{cases} P(i, i) = \text{true} \\ P(i, i+1) = ( S_i == S_{i+1} ) \end{cases}
{ 
P(i,i)=true
P(i,i+1)=(S 
i
​
 ==S 
i+1
​
 )
​
 
根据这个思路，我们就可以完成动态规划了，最终的答案即为所有 P(i,j)=trueP(i, j) = \text{true}P(i,j)=true 中 j−i+1j-i+1j−i+1（即子串长度）的最大值。注意：在状态转移方程中，我们是从长度较短的字符串向长度较长的字符串进行转移的，因此一定要注意动态规划的循环顺序。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                    
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]

# 可以发现，所有的状态在转移的时候的可能性都是唯一的。也就是说，我们可以从每一种边界情况开始「扩展」，也可以得出所有的状态对应的答案。

# 边界情况即为子串长度为 111 或 222 的情况。我们枚举每一种边界情况，并从对应的子串开始不断地向两边扩展。如果两边的字母相同，我们就可以继续扩展，例如从 P(i+1,j−1)P(i+1,j-1)P(i+1,j−1) 扩展到 P(i,j)P(i,j)P(i,j)；如果两边的字母不同，我们就可以停止扩展，因为在这之后的子串都不能是回文串了。

# 聪明的读者此时应该可以发现，「边界情况」对应的子串实际上就是我们「扩展」出的回文串的「回文中心」。方法二的本质即为：我们枚举所有的「回文中心」并尝试「扩展」，直到无法扩展为止，此时的回文串长度即为此「回文中心」下的最长回文串长度。我们对所有的长度求出最大值，即可得到最终的答案。
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]
