"""
HJ2 计算某字符出现次数
题目
题解(1k)
讨论(2k)
排行
面经new
简单  通过率：31.26%  时间限制：1秒  空间限制：32M
知识点
字符串
哈希
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）

数据范围：
1
≤
�
≤
1000

1≤n≤1000
输入描述：
第一行输入一个由字母、数字和空格组成的字符串，第二行输入一个字符（保证该字符不为空格）。

输出描述：
输出输入字符串中含有该字符的个数。（不区分大小写字母）

示例1
输入：
ABCabc
A
复制
输出：
2
复制
"""
string_str = input().lower()
char = input().lower()
char_count = 0
for s in string_str:
    if s == char:
        char_count += 1
print(char_count)