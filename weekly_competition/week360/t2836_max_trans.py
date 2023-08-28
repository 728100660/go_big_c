"""
n = len(receiver)
        m = k.bit_length() - 1
        pa = [[(p, p)] + [None] * m for p in receiver]
        for i in range(m):
            for x in range(n):
                p, s = pa[x][i]
                pp, ss = pa[p][i]
                pa[x][i + 1] = (pp, s + ss)  # 合并节点值之和

        ans = 0
        for i in range(n):
            x = sum = i
            for j in range(m + 1):
                if (k >> j) & 1:  # k 的二进制从低到高第 j 位是 1
                    x, s = pa[x][j]
                    sum += s
            ans = max(ans, sum)
        return ans

"""
"""
传球游戏中最大化函数值

给定传球次数k，传球列表receiver，自己选定从某个节点开始，返回传球之和
k = 1的事后，选择idx=2作为起始 传球之和 = idx +  receiver[idx] = 3

输入：receiver = [2,0,1], k = 4
输出：6

输入：receiver = [1,1,1,2,3], k = 3
输出：10

pa[x][i]: 存储着从x出发的第2**i个节点的位置和路径和
pa[x][0] = parent[x]    # 父节点   1
pa[x][1] = pa[pa[x][0]][0]  # 父节点的父节点   2
pa[x][2] = pa[pa[x][1]][1]  # 爷爷节点的爷爷节点 4
....

"""
from typing import List


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        total_count = k.bit_length() - 1    # 例如4, 4的bit_len=3，但实际上直走到 2**2
        num_len = len(receiver)
        dp = [[(0,0)] * (total_count+1) for _ in range(num_len)]
        for i in range(total_count+1):    # 确保之后的节点都访问了，所以这里从i开始遍历而不是x
            for x in range(num_len):
                if i == 0:
                    # 往上走1个节点，即为receiver指向的节点，receiver[x]位到达路径和，
                    # 注意：不能写成x+receiver[x] 下标值不能写在这，否则会重复添加，在结果写下标值
                    dp[x][i] = (receiver[x], receiver[x])
                    continue
                pos, path_sum = dp[x][i-1]        # 往上走2**i-1个节点走到pos
                pos2, path_sum2 = dp[pos][i-1]    # pos再往上走2**i-1个节点走到 2**i个节点，走到pos2，所以dp[x][i] = pos2
                dp[x][i] = (pos2, path_sum + path_sum2)

        # 枚举，找到符合要求的最大值
        ans = 0
        for start in range(num_len):
            x = max_sum = start     # 初始和为下标
            for i in range(total_count+1):
                if (k >> i) & 1 == 1:    # k的二进制第i位为1
                    x, s = dp[x][i]     # 拿到从x出发的第2**i个节点并且更新x的值
                    max_sum += s
            ans = max(max_sum, ans)
        return ans


if __name__ == '__main__':
    oSolute = Solution()
    assert oSolute.getMaxFunctionValue([2, 0, 1], 4) == 6
    assert oSolute.getMaxFunctionValue([1, 1, 1, 2, 3], 3) == 10