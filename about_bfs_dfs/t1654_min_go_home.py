"""
到家最小跳跃次数
1654. 到家的最少跳跃次数
提示
中等
122
相关企业
有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。

跳蚤跳跃的规则如下：

它可以 往前 跳恰好 a 个位置（即往右跳）。
它可以 往后 跳恰好 b 个位置（即往左跳）。
它不能 连续 往后跳 2 次。
它不能跳到任何 forbidden 数组中的位置。
跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。

给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，请你返回跳蚤到家的最少跳跃次数。
如果没有恰好到达 x 的可行方案，请你返回 -1 。



示例 1：

输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
输出：3
解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。
示例 2：

输入：forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
输出：-1
示例 3：

输入：forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
输出：2
解释：往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。

forbidden=[162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
a=29,b=98,x=80
res=121


提示：

1 <= forbidden.length <= 1000
1 <= a, b, forbidden[i] <= 2000
0 <= x <= 2000
forbidden 中所有位置互不相同。
位置 x 不在 forbidden 中。
通过次数
13K
提交次数
38.2K
通过率
34.1%
"""
from typing import List

"""
思路1：动态规划(错误的)
dp[i] 表示跳到第i个格子上所需要最小次数
dp[i] 可以由前进得来，也可以由后退得来，
先遍历一遍前进的，再遍历一遍后退的(这样能确保只后退一次，)，
注意判断forbidden

初始化dp[i] = 2000     # 最多都不可能跳2000步数

dp[i] = min(dp[i-a] + 1, dp[i+b] + 1)

思路2：BFS（广度优先）
在一个节点就两个选择：向前跳a步，向后跳b步，
难点
不能连续向后跳两次: bfs队列中加一个存储flag标记是否由向后跳得来的
如何判断step?  两层循环遍历queue，一个step对应一层
注意，向后跳得到的节点和向前跳的的到的节点不是同一个，因此visite_set需要记录方向，其实可以用num * +-1 解决
确定向前跳的上限：upper    看不懂，以后这种题目直接把你知道的所有值加起来就行了, 蒙就完事了， max(forbidden) + a + b + x，总有一个能对
"""

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_set = {i for i in forbidden}
        upper = max(max(forbidden) + a, x) + b
        visit_set = set()
        queue = [(0, 0)]
        step = 0
        while queue:
            for _ in range(len(queue)):     # for循环很重要，以遍历该步数能到达的节点
                pos, is_back_pos = queue.pop(0)     # 节点位置，是否向后跳得来的节点
                ## 判断是否目标节点
                if pos == x:
                    return step
                # 向前跳: 不在forbidden中，未访问过，不超过边界
                forward_jump = pos + a
                if forward_jump not in forbidden_set and forward_jump <= upper:
                    if (forward_jump, 0) not in visit_set:
                        queue.append((forward_jump, 0))
                        visit_set.add((forward_jump, 0))

                # 向后跳: 不在forbidden中，未访问过，不超过边界，不是向后跳得来的
                backward_jump = pos - b
                if not is_back_pos and backward_jump not in forbidden_set and backward_jump >= 0:
                    if (backward_jump, 1) not in visit_set:
                        queue.append((backward_jump, 1))
                        visit_set.add((backward_jump, 1))
            step += 1
        return -1


if __name__ == '__main__':
    oSolution = Solution()
    as4 = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
    assert oSolution.minimumJumps(forbidden = as4, a = 29, b = 98, x = 80) == 121
    assert oSolution.minimumJumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7) == 2
    assert oSolution.minimumJumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9) == 3
    assert oSolution.minimumJumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11) == -1
