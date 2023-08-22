"""
恢复数字序列
题目描述
对于一个连续正整数组成的序列，可以将其拼接成一个字符串，再将字符串里的部分字符打乱顺序。如序列
8 9 10 11 12，拼接成的字符串为 89101112，打乱一部分字符后得到90811211，原来的正整数
10就被拆成了
0和1。 现给定一个按如上规则得到的打乱字符的字符串，请将其还原成连续正整数序列，并输出序列中最小的数字。

输入描述
输入一行，为打乱字符的字符串和正整数序列的长度，两者间用空格分隔，字符串长度不超过
200，正整数不超过
1000，保证输入可以还原成唯一序列。

输出描述
输出一个数字，为序列中最小的数字。

样例
输入

19801211 5
输出

8
说明

无。

"""

"""
输入序列 str， 数字个数 为n
连续正整数
数字最大值位数不超过  (len(str)+ (n-1)) / n    向上取整
数字最小值位数不小于  len(str) // n

太复杂了，网上搜了下，居然是暴力解法，离谱

map记录各个数字出现的个数
判断起始位数 = len(string) / num
从起始位开始枚举，符合条件就是答案
"""


def main():
    string, num_count = input().split()
    num_count = int(num_count)

    min_wei = len(string) // num_count  # 起始位数
    if min_wei == 1:
        start_num = 0
    else:
        start_num = 10**(min_wei-1)
    # 初始化计数map
    words_count_info = {s: 0 for s in range(10)}
    for s in string:
        words_count_info[int(s)] += 1

    # 暴力
    while start_num<=1000:
        tmp_count_map = {s: 0 for s in range(10)}
        for offset in range(num_count):      # 往后找num_count-1个数字
            num = start_num + offset
            while num:
                tmp_count_map[num % 10] += 1
                num = num // 10
        if tmp_count_map == words_count_info:
            return start_num
        start_num += 1      # 每回合增加起始值，遍历
    return 0


print(main())
