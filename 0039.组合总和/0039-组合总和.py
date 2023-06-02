变量意义：use表示已经使用过的数（组成的列表），remain表示距离target还有多大。

对candidates升序排序，以方便根据remain的大小使用return减小搜索空间；
递归求可能的组合。具体的，每次递归时对所有candidates做一次遍历，情况有3：1，满足条件，则答案加入一条；2，不足，继续递归，3，超出，则直接退出本路线。
注意每层递归都对全体candidates做遍历会导致如[2,2,3],[3,2,2]这样的对称重复的答案的产生。这是因为发生了“往前选择”的情况，我们每次更深层的递归都往后缩小一个candidates，强制函数只能“往后选择”，这将不会出现重复答案。
代码写的比较简单，更多细节请看代码


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        ans = []

        def find(s, use, remain):
            for i in range(s, len(candidates)):
                c = candidates[i]
                if c == remain:
                    ans.append(use + [c])
                if c < remain:
                    find(i, use + [c], remain - c)
                if c > remain:
                    return
        find(0, [], target)

        return ans

