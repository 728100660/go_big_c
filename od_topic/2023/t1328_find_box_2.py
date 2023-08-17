"""
题目描述
一贫如洗的樵夫阿里巴巴在去砍柴的路上，无意中发现了强盗集团的藏宝地，藏宝地有编号从
0−N的箱子，每个箱子上面贴有箱子中藏有金币
Q的数量。 从金币数量中选出一个数字集合，并销毁贴有这些数字的每个箱子，如果能销毁一半及以上的箱子，则返回这个数字集合的最小大小

输入描述
第一行1个数字字串，数字之间使用逗号分隔，例如:
6,6,6,6,3,3,3,1,1,5字串中数字的个数为偶数，并且
1≤字串中数字的个数≤100000
1≤每个数字≤100000
输出描述
这个数字集合的最小大小

样例
输入

1,1,1,1,3,3,3,6,6,8
输出

2
说明

选择集合
1,8，销毁后的结果数组为[3,3,3,6,6]，长度为
5，长度为原数组的一半。

大小为
2 的可行集合还有{1,3},{1,6},{3,6}。

选择6,8集合是不可行的，它销后的结果数组为
[1,1,1,1,3,3,3]，新数组长度大于原数组的二分之一。

输入

2,2,2,2
输出

1
说明

我们只能选择集合{2}，销毁后的结果数组为空。
"""


def main():
    box_list = list(map(int, input().split(",")))
    box_num_map = {}
    for box in box_list:
        if box not in box_num_map:
            box_num_map[box] = 1
            continue
        box_num_map[box] += 1
    box_count_list = sorted(box_num_map.values())   # 箱子种类个数列表

    half = len(box_list) // 2
    total_count = 0
    choose_type_count = 0   # 选择种类数
    for count in box_count_list[::-1]:
        total_count += count
        choose_type_count += 1
        if total_count >= half:
            return choose_type_count
    return choose_type_count


print(main())
