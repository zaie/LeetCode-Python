在每个状态下，无论长板或短板向中间收窄一格，都会导致水槽 底边宽度 −1-1−1​ 变短：

若向内 移动短板 ，水槽的短板 min(h[i],h[j])min(h[i], h[j])min(h[i],h[j]) 可能变大，因此下个水槽的面积 可能增大 。
若向内 移动长板 ，水槽的短板 min(h[i],h[j])min(h[i], h[j])min(h[i],h[j])​ 不变或变小，因此下个水槽的面积 一定变小 。
因此，初始化双指针分列水槽左右两端，循环每轮将短板向内移动一格，并更新面积最大值，直到两指针相遇时跳出；即可获得最大面积。

算法流程：
初始化： 双指针 iii , jjj 分列水槽左右两端；
循环收窄： 直至双指针相遇时跳出；
更新面积最大值 resresres ；
选定两板高度中的短板，向中间收窄一格；
返回值： 返回面积最大值 resresres 即可；


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
