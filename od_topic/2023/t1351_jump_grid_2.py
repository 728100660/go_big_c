"""
题目描述
小明和朋友玩跳格子游戏，有
n个连续格子组成的圆圈，每个格子有不同的分数，小朋友可以选择以任意格子起跳，但是不能跳连续的格子，不能回头跳，也不能超过一圈;

给定一个代表每个格子得分的非负整数数组，计算能够得到的最高分数。

输入描述
给定一个数例，第一个格子和最后一个格子首尾相连，如:
2 3 2

输出描述
输出能够得到的最高分，如:
3

备注
1≤nums.length≤100
1≤nums[i]≤1000
样例
输入

2 3 2
输出

3
说明

只能跳
3
3这个格子,因为第一个格子和第三个格子首位相连

输入

1 2 3 1
输出

4
说明
1+3=4
"""

"""
思路：一条从0下标出发，不统计-1下标，一条从1下标出发，统计-1, 然后选出两条路线的最大值
动态规划
1. 初始化
2. 状态转移   dp[i] = max(dp[i-2], dp[i-3) + cur_val

# 错误点：
计算第二条路线的时候误解了idx的概念，导致取数错误，取数应该是val而不是grid_list[idx]
"""

def main():
    grid_list = list(map(int, input().split(" ")))
    if len(grid_list) == 1:
        print(0)
        return 0
    if len(grid_list) <= 3:
        print(max(grid_list))
        return
    # 从索引0到-2的dp
    dp = grid_list[:3]
    dp[2] = dp[0] + dp[2]
    for idx in range(3, len(grid_list)-1):
        dp.append(max(dp[idx-2], dp[idx-3]) + grid_list[idx])
    dp1_max = max(dp[-1], dp[-2])
    # 从索引1到-1的dp
    dp2 = []
    for idx, val in enumerate(grid_list[1:]):
        if idx < 2:
            dp2.append(val)
        elif idx == 2:
            dp2.append(dp2[idx-2] + val)
        else:
            dp2.append(max(dp2[idx-2], dp2[idx-3]) + val)
    dp2_max = max(dp2[-1], dp2[-2])
    print(max(dp2_max, dp1_max))


main()