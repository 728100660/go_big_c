"""
五子棋迷
题目描述
张兵和王武是五子棋迷，工作之余经堂切磋棋艺。这不，这会儿又下起来了。走了一会儿，轮张兵了，对着一条线思考起来了，这条线上的棋子分布如下:

用数组表示:-101110101-1

棋了分布说明:

--1代表白子，0代表空位，1代表黑子

数组长度L，满足1<L< 40，L为奇数
你得帮他写一个程序，算出最有利的出子位置。 最有利定义:

找到一个空位(0)，用棋子(1/-1)填充该位置，可以使得当前子的最大连续长度变大
如果存在多个位置，返回最靠近中间的较小的那个坐标
如果不存在可行位置，直接返回-1
连续长度不能超过5个(五字棋约束)
输入描述
第一行: 当前出子颜色。 第二行: 当前的棋局状态。

输出描述
1个整数，表示出子位置的数组下标

样例
输入

1
-1 0 1 1 1 0 1 -1 1
输出

5
说明

当前为黑子(1)，放置在下标为5的位置，黑子的最大连续长度，可以由3到5

输入

-1
-1 0 1 1 1 0 1 0 1 -1 1
输出

1
说明

当前为白子，唯一可以放置的位置下标为1，白字的最大长度，由1变为2

输入

1
0 0 0 0 1 0 0 0 0 1 0
输出

5
说明

可以的位置很多，5最接近中间的位置坐标


=====
1
0 1 1 1 1 1 0 0 -1 1 0 1 1 0
-1
======

"""

"""
抛弃常识，按照他说的做就行
说不能超过五个就不能超过五个
注意需要满足：使得当前子的最大连续长度变大
"""
def main():
    color = int(input())
    grid = list(map(int, input().split(" ")))
    # 遍历，找到每个空位判断是否能下子
    # 其他子，跳过
    # 当前子，记录长度
    # 空，看前后，记录长度，判断能否下子
    mid = len(grid) // 2    # 中间位置
    pos = -1     # 落子位置

    # 初始化当前子的最大长度
    max_len = 0     # 最大长度
    pre_max = 0
    for grid_color in grid:
        if grid_color != color:
            pre_max = 0
            continue
        pre_max = pre_max + 1
        max_len = max(pre_max, max_len)
    # 标记最大长度是否增长过
    add_flag = 0

    for idx, grid_color in enumerate(grid):
        if grid_color != 0:
            continue
        grid_len = 1    # 本次落子长度
        tmp_idx = idx - 1
        while tmp_idx >= 0 and grid[tmp_idx] == color:
            grid_len += 1
            tmp_idx -= 1
        tmp_idx = idx + 1
        while tmp_idx < len(grid) and grid[tmp_idx] == color:
            grid_len += 1
            tmp_idx += 1
        if grid_len > 5 or grid_len == 1:        # 长度大于5或者周围没有同颜色子
            continue
        if grid_len > max_len:
            pos = idx
            max_len = grid_len
            add_flag = 1
        elif grid_len == max_len:
            if abs(mid - idx) < abs(mid - pos):     # 此次落点更加居中
                pos = idx
                max_len = grid_len
            elif abs(mid - idx) == abs(mid - pos) and idx < pos:    # 同等距离取idx小的
                pos = idx
                max_len = grid_len
    if add_flag:
        print(pos)
    else:
        print(-1)

main()
