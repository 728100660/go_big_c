"""
剑指 Offer 10- I. 斐波那契数列
简单
502
相关企业
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。



示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5


提示：

0 <= n <= 100
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        fib_list = [1, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list[-1]


if __name__ == '__main__':
    oSolute = Solution()
    assert oSolute.fib(5) == 5
    assert oSolute.fib(2) == 1