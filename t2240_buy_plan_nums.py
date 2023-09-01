"""
买铅笔和钢笔的方案数
给你一个整数 total ，表示你拥有的总钱数。同时给你两个整数 cost1 和 cost2 ，分别表示一支钢笔和一支铅笔的价格。你可以花费你部分或者全部的钱，去买任意数目的两种笔。

请你返回购买钢笔和铅笔的 不同方案数目 。



示例 1：

输入：total = 20, cost1 = 10, cost2 = 5
输出：9
解释：一支钢笔的价格为 10 ，一支铅笔的价格为 5 。
- 如果你买 0 支钢笔，那么你可以买 0 ，1 ，2 ，3 或者 4 支铅笔。
- 如果你买 1 支钢笔，那么你可以买 0 ，1 或者 2 支铅笔。
- 如果你买 2 支钢笔，那么你没法买任何铅笔。
所以买钢笔和铅笔的总方案数为 5 + 3 + 1 = 9 种。
示例 2：

输入：total = 5, cost1 = 10, cost2 = 10
输出：1
解释：钢笔和铅笔的价格都为 10 ，都比拥有的钱数多，所以你没法购买任何文具。所以只有 1 种方案：买 0 支钢笔和 0 支铅笔。

1 <= total, cost1, cost2 <= 10**6
"""
"""
动态规划(错误思路)
1. dp[i]: 价格为i的时候的最大方案数
2. dp[i]可以由买一只钢笔或者买一只铅笔得来, 所以
   dp[i] = dp[i-cost1] + dp[i-cost2]
3. 初始化 默认所有价格都有一种方案: 0 支钢笔和 0 支铅笔

枚举
按照方案数枚举
"""


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 1    # 方案数目
        plan_num = (((total + cost1 - 1) / cost1) * ((total + cost1 - 1) / cost1))


if __name__ == '__main__':
    oSolution = Solution()
    assert oSolution.waysToBuyPensPencils(20, 10, 5) == 9
    assert oSolution.waysToBuyPensPencils(5, 10, 10) == 1
