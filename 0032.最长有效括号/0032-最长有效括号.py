# 思路
# 栈的功能：栈存储索引。在遍历过程中，只要有两个连续索引对应字符可以构成一对括号就出栈，这样栈中存储的都是到当前位置暂时不可以构成括号的索引。

# 那满足什么条件才会导致当前不可以构成括号呢？
# i. 当前栈为空。当前字符s[i]将会是栈中第一个字符，无法跟之前的字符构成一对括号
# ii. 当前字符s[i]是左括号'('。左括号无法跟栈顶元素构成一对括号
# iii. 栈顶元素是右括号')'。无论当前字符s[i]是什么，都无法和栈顶元素构成一对括号

# 其实也就是栈顶元素必须为'('，当前字符s[i]必须为')'，这样才能构成一对括号

# 构成一对括号以后，栈顶元素出栈。
# 这样就可以满足前面说的栈中存储的都是当前暂时不可以构成括号的索引

# 当前有效括号的长度 = 当前索引i - 栈顶存储的索引stack[-1]
# 最后要返回的最长有效括号长度即为res = max(res, i - stack[-1])
# 因为此时栈可能为空，如果为空就是res = max(res, i - (-1))

# 时间复杂度：O(n)O(n)
# 空间复杂度：O(n)O(n)

# 作者：edelweisskoko
# 链接：https://leetcode-cn.com/problems/longest-valid-parentheses/solution/32-zui-chang-you-xiao-gua-hao-fu-zhu-zha-1cqq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        res = 0
        for i, x in enumerate(s):
            if x == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
#             print(stack)
                    
        return res
