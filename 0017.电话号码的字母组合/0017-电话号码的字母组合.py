当题目中出现 “所有组合” 等类似字眼时，我们第一感觉就要想到用回溯。

定义函数 backtrack(combination, nextdigit)，当 nextdigit 非空时，对于 nextdigit[0] 中的每一个字母 letter，
执行回溯 backtrack(combination + letter,nextdigit[1:]，直至 nextdigit 为空。最后将 combination 加入到结果中。


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
                
        def backtrack(conbination,nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination + letter,nextdigit[1:])

        res = []
        backtrack('',digits)
        return res
