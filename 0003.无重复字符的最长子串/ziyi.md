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
        
![image](https://github.com/zaie/LeetCode-Python/assets/17739876/5a4f060e-a10a-4587-89d2-d983f7fd411e)
