# 双指针，如果没有重复就扩大（就动左指针），记录最大长度
# 否则就动右指针，直到没有重复为止
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        res = 0
        if len(s) == 0:
            return 0
        if s.count(s[0]) == len(s):
            return 1
        if len(set(s)) == len(s):
            return len(s)
        while right < len(s):
            if s[right] not in s[left:right]:
                right +=1
                res = max(res,len(s[left:right]))
            else:
                while s[right] in s[left:right]:
                    left +=1
        return res
