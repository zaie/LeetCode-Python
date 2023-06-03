参数定义
m,n：矩阵行列数
pre：长度为n+1，初始值为0的数组，记录每个位置上方（包含当前位置）连续1的个数，最后一个位置为0，便于单调栈处理
stack：单调栈，存储元素的索引，且索引对应的元素单调递增

思路                               
前缀和思想求连续1的个数：
对于pre的计算，当前位置j为0，则pre[j]=0，当前位置为1，则需要加上上一层连续1的个数，即pre[j]+=1。
如第二行（下标从0开始）pre[2]=[3,1,3,2,2,0]，最后多一个0便于单调栈处理
单调栈计算最大矩形：
初始化栈，存入下标-1，便于处理所有元素弹出栈后的情况
当栈顶索引index对应的元素pre[index]大于当前索引为k的元素num时，将栈顶元素index弹出，因为栈中索引对应的值是单调递增的，所以此时栈顶元素stack[-1]到k-1之间的数均是不小于pre[index]的，此时以pre[index]为高的矩阵的长度为k-stack[-1]-1，面积S=pre[index]*(k-stack[-1]-1)
pre数组末尾添加0的目的，就是能将所有元素弹出栈，从而计算所有矩阵面积
利用res记录最大矩阵面积

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:return 0
        m,n=len(matrix),len(matrix[0])
        # 记录当前位置上方连续“1”的个数
        pre=[0]*(n+1)
        res=0
        for i in range(m):
            for j in range(n):
                # 前缀和
                pre[j]=pre[j]+1 if matrix[i][j]=="1" else 0

            # 单调栈
            stack=[-1]
            for k,num in enumerate(pre):
                while stack and pre[stack[-1]]>num:
                    index=stack.pop()
                    res=max(res,pre[index]*(k-stack[-1]-1))
                stack.append(k)

        return res

# 作者：追风少年
# 链接：https://leetcode.cn/problems/maximal-rectangle/solutions/535898/python3-qian-zhui-he-dan-diao-zhan-ji-su-vkpp/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
