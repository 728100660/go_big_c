"""
剑指 Offer 10- II. 青蛙跳台阶问题
简单
407
相关企业
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100
"""

"""
思路
一个数组，idx为第n级台阶，val为对应台阶的方法
第n个台阶的方法数为n-1 + n-2的和
"""
class Solution:
    def numWays(self, n: int) -> int:
        ways_list = [0, 1, 2]
        for i in range(3, n + 1):
            ways_list.append((ways_list[i-1] + ways_list[i-2]) % 1000000007)
        return ways_list[n]


if __name__ == '__main__':
    oSolute = Solution()
    assert oSolute.numWays(2) == 2
    assert oSolute.numWays(7) == 21
