"""
阿里巴巴找黄金宝箱4
题目描述
贫如洗的椎夫阿里巴巴在去砍柴的路上，无意中发现了强盗集团的藏宝地，藏宝地有编号从
0−N的箱子，每个箱子上面有一个数字，箱了排列成一个环，编号最大的箱子的下一个是编号为
0的箱子。

请输出每个箱子贴的数字之后的第一个比它大的数，如果不存在则输出
−1。

输入描述
输入一个数字字串，数字之间使用逗号分隔，例如:
1,2,3,1
1≤字串中数字个数≤10000:
−100000≤每个数字值≤10000:
输出描述
下一个大的数列表，以逗号分隔，例如:
2,3,6,−1,6

样例
输入

2,5,2
输出

5,-1,5
说明

第一个2的下一个更大的数是5；

数字5找不到下一个更大的数；

第二个
2的下一个最大的数需要循环搜索，结果也是5

输入

3,4,5,6,3
输出

4,5,6,-1,4
说明

无
"""

"""
思路：没有
只会暴力，但是估计超时

使用单调栈解决
下一个更大数(单调递减栈)，下一个更小数，使用单调栈解决

stack 存下标
当前下标idx
nums[idx] <= nums[stack[-1]]时 入栈
nums[idx] > nums[stack[-1]]时 出栈

循环问题，找两遍，第二遍直到 stack[-1]下标(栈顶的下标肯定比栈底的下标大，至此第二遍遍历完毕)
"""


def main():
    nums = list(map(int, input().split(",")))
    res = [-1] * len(nums)
    # 下标栈
    stack = []
    # 第一遍正常遍历
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    # 第二遍只pop不append
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            res[stack.pop()] = nums[i]
    return ",".join(map(str, res))


print(main())

