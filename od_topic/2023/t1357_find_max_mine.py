"""
寻找最大价值矿堆
题目描述
给你一个由'0'(空地)、'1'(银矿)、'2'金矿)组成的的地图，矿堆只能由上下左右相邻的金矿或银矿连接形成。超出地图范围可以认为是空地。

假设银矿价值1，金矿价值2 ，请你找出地图中最大价值的矿堆并输出该矿堆的价值.

输入描述
地图元素信息如:

22220
00000
00000
11111
地图范围最大 300∗300
0≤地图元素≤2
输出描述
矿堆的最大价值

样例
输入

22220
00000
00000
01111
输出

8
说明

无

输入

22220
00020
00010
01111
输出

15
说明

无

输入

20000
00020
00000
00111
break
输出

3
说明

无
"""

"""
思路：bfs
"""
import sys


def get_i_j(mine_grid, i, j):
    try:
        return mine_grid[i][j]
    except Exception:
        return 0


def bfs(mine_grid, i, j):
    try:
        if not (0 <= i < len(mine_grid) and 0 <= j < len(mine_grid[0])):
            return 0
        if get_i_j(mine_grid, i, j) == 0:
            return 0
        this_val = get_i_j(mine_grid, i, j)
        mine_grid[i][j] = 0  # 标记为0，防止重复进入
        return this_val + \
               bfs(mine_grid, i - 1, j) + \
               bfs(mine_grid, i + 1, j) + \
               bfs(mine_grid, i, j - 1) + \
               bfs(mine_grid, i, j + 1)
    except Exception:
        return 0


def main():
    if not mine_grid:
        return 0
    if not mine_grid[0]:
        return 0
    res = 0  # 最大矿堆价值
    for i in range(len(mine_grid)):
        for j in range(len(mine_grid[0])):
            res = max(bfs(mine_grid, i, j), res)
    return res


# mine_grid = []
# for line in sys.stdin:
#     tmp_grid = []
#     tmp_str = line.strip()
#     for s in tmp_str:
#         s = int(s)
#         tmp_grid.append(s)
#     if tmp_grid:
#         mine_grid.append(tmp_grid)

mine_grid = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]  # 示例输入，你可以根据需要修改

print(main())
