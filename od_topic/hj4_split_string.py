"""
HJ4 字符串分隔
题目
题解(1k)
讨论(2k)
排行
面经new
简单  通过率：28.26%  时间限制：1秒  空间限制：32M
知识点
字符串
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；

•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述：
连续输入字符串(每个字符串长度小于等于100)

输出描述：
依次输出所有分割后的长度为8的新字符串

示例1
输入：
abc
复制
输出：
abc00000
"""
handle_str = input()
each_list = []  # 8个字符的暂存数组
for idx, s in enumerate(handle_str):
    if idx != 0 and idx % 8 == 0:    # 说明已经遍历了8个字符了
        print("".join(each_list))
        each_list = []
    each_list.append(s)
if each_list:   # 最后几个字符
    tmp_str = "".join(each_list)
    tmp_str = tmp_str.ljust(8, "0")
    print(tmp_str)