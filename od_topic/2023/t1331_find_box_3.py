"""
题目描述
贫如洗的樵夫阿里巴巴在去砍柴的路上，无意中发现了强盗集团的藏宝地，藏宝地有编号从
0−N的箱子，每个箱子上面贴有一个数字。
阿里巴巴念出一个咒语数字，查看宝箱是否存在两个不同箱子，这两个箱子上贴的数字相同，同时这两个箱了的编号之差的绝对值小于等于咒语数字，
如果存在这样的一对宝箱，请返回最先找到的那对宝箱左边箱子的编号，如果不存在则返回
−1

输入描述
第一行输入一个数字字串，数字之间使用逗号分隔，例如:
1,2,3,1
1≤字串中数字个数 ≤100000
−100000≤每个数字值≤100000
第二行输入咒语数字，例如:
3

1≤ 咒语数字 ≤100000
输出描述
存在这样的一对宝箱，请返回最先找到的那对宝箱左边箱子的编号，如果不存在则返回
−1

样例
输入

6,3,1,6
3
输出

0
说明

无

输入

5,6,7,5,6,7
2
输出

-1
说明

无
"""

"""
没啥思路，用map，按照题意去解
题目意思并不是第一个找到的一对数字，而是左边数字下标最小的那一对数字    属于是曲解题意了
"""


def main():
    box_list = list(map(int, input().split(",")))
    magic_num = int(input())    # 魔法数字
    box_idx_map = {}       # 箱子以及下标映射表
    min_idx = len(box_list)
    for idx, box_num in enumerate(box_list):
        if box_num not in box_idx_map:
            box_idx_map[box_num] = idx
        else:
            # 与咒语数字比较判断是否返回， <= 则返回左边编号，否则继续
            if idx - box_idx_map[box_num] <= magic_num:
                if box_idx_map[box_num] < min_idx:
                    min_idx = box_idx_map[box_num]       # 记录结果
            box_idx_map[box_num] = idx
    return min_idx if min_idx != len(box_list) else -1


print(main())
