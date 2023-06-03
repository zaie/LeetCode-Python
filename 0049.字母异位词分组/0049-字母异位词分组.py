# 主要是dict.get()函数的理解 dict.get(key, default=None) 1. key -- 字典中要查找的键。 
# 2. default -- 如果指定键的值不存在时，返回该默认值。

# 还有一点要注意：因为字典的键，必须是不可变类型，所以用tuple。

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())

# 作者：梦之痕
# 链接：https://leetcode.cn/problems/group-anagrams/solutions/254945/python3-99-by-meng-zhi-hen-n/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
            
                
