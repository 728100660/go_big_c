"""
剑指 Offer 17. 打印从1到最大的n位数
简单
304
相关企业
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]


说明：

用返回一个整数列表来代替打印
n 为正整数
"""
from typing import List

"""
真正的分治是用递归的思路解决问题，这个就这样吧
"""
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i+1 for i in range(10**n-1)]