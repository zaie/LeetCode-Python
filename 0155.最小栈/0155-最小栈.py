class MinStack:
    
    def __init__(self):
        self.data = [(None, float('inf'))]

    def push(self, x: 'int') -> 'None':
        self.data.append((x, min(x, self.data[-1][1])))

    def pop(self) -> 'None':
        if len(self.data) > 1: self.data.pop()

    def top(self) -> 'int':
        return self.data[-1][0]

    def getMin(self) -> 'int':
        return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# 作者：
# 链接：https://leetcode.cn/problems/min-stack/solutions/4114/python-mei-ge-yi-xing-by-knifezhu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
