"""
剑指 Offer 63. 股票的最大利润
中等
362
相关企业
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？



示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


限制：

0 <= 数组长度 <= 10^5
"""
"""
动态规划
1. 初始化数组
2. 第n天，要么卖，要么不卖，不卖就等于n-1天的收益，卖就等于当天价格减前n天的最小价格 状态转移方程: 
   dp[n] = max(dp[n-1], price[n] - min_price) 
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        dp = [0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            dp.append(max(dp[i-1], prices[i]-min_price))
        return dp[len(prices)-1]
