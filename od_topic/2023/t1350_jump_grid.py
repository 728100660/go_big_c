"""
题目描述
小明和朋友玩跳格子游戏，有n个连续格子，每个格子有不同的分数，小朋友可以选择以任意格子起跳，但是不能跳连续的格子，也不能回头跳;

给定一个代表每个格子得分的非负整数数组，计算能够得到的最高分数。

输入描述
给定一个数列，如:
1 2 3 1

输出描述
输出能够得到的最高分，如:
4

备注
1≤nums.length≤100
0≤numsli]≤1000

样例
输入

1 2 3 1
输出

4
说明

选择跳第一个格子和第三个格子

输入

2 7 9 3 1
输出

12
说明

2 + 9 + 1 = 12
2+9+1=12
"""

"""
一眼动态规划，跟力扣青蛙跳台阶类似
1. 初始化dp = [] : 表示跳到当前位置的最大总得分
2. 状态转移，不能连续且要得分最高，那么最多跳三格，不可能跳四格，跳四格等于跳两个两格，显然两个两格更大
    dp[i] = max(dp[i-2], dp[i-3]) + cur_val
"""

def main():
    grid_list = list(map(int, input().split(" ")))
    if len(grid_list) < 3:
        print(max(grid_list))
        return
    # 初始化
    dp = grid_list[:3]
    dp[2] = dp[0] + dp[2]
    for idx in range(3, len(grid_list)):
        dp.append(max(dp[idx-2], dp[idx-3]) + grid_list[idx])

    print(max(dp[-1], dp[-2]))  # 倒数第一个并不能代表所有路径，要加上倒数第二个



main()