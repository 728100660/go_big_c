"""
HJ5 进制转换
题目
题解(1k)
讨论(1k)
排行
面经new
简单  通过率：35.77%  时间限制：1秒  空间限制：32M
知识点
字符串
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

数据范围：保证结果在
1
≤
�
≤
2
31
−
1

1≤n≤2
31
 −1
输入描述：
输入一个十六进制的数值字符串。

输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。

示例1
输入：
0xAA
复制
输出：
170
复制
"""
hex_str = input()
str_val_map = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}
# 从右往左开始遍历
res = 0
for idx, s in enumerate(hex_str[:1:-1]):
    res += str_val_map[s] * 16**idx
print(res% (2**31-1))