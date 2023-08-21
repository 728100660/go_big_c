"""
座位调整
题目描述
疫情期间课堂的座位进行了特殊的调整，不能出现两个同学紧挨着，必须隔至少一个空位。

给你一个整数数组 desk 表示当前座位的占座情况，由若于
0和1组成，其中 0 表示没有占位，1表示占位。

在不改变原有座位秩序情况下，还能安排坐几个人?

输入描述
第一行是个子数组表示作为占座情况，由若干 0和 1组成，其中0 表示没有占位，1 表示占位

输出描述
输出数值表示还能坐几个人。

备注
1≤desk.length≤2*10**4


样例
输入

1,0,0,0,1
输出

1
说明

只有
desk[2]的位置可以坐一个人。

0,0,0,0,1,1,0,1,0,0,0,0
4

0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0
"""

"""
找出两个相邻的1间隔多少个座位n，  中间可坐的人为 (n - 1)// 2
直到结束，
结束for循环后还要判断一次

注意：以后循环递增的变量一定要注释标识，防止忘记
"""
def main():
    seats = list(map(int, input().split(",")))
    pre_1_idx = -1       # 上一个1的下标
    peoples = 0     # 可以坐的人数
    for idx, seat in enumerate(seats):
        if seat != 1:
            continue
        # 计算中间可坐的人数，并更新下标
        diff_seat = idx - pre_1_idx - 1     # 相隔0的个数, 3 - 1 = 2， 但其实中间只有一个格子
        if diff_seat == 0:
            pass
        elif pre_1_idx == -1:     # 3个0,2个0的结果都是1
            peoples += diff_seat // 2
        else:
            peoples += (diff_seat - 1) // 2     # 3个0,4个0的结果都是1
        pre_1_idx = idx
    left_zero_num = len(seats) - 1 - pre_1_idx
    if pre_1_idx == -1:         # 数组中没有人占座
        peoples += left_zero_num + 1 // 2   # 向上取整， 5个0,4个0，结果都为3
    else:
        peoples += left_zero_num // 2   # 向下取整
    return peoples


print(main())
