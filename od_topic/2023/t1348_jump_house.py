"""
跳房子，也叫跳飞机，是一种世界性的儿童游戏

游戏参与者需要分多个回合按顺序跳到第1格直到房子的最后一格。

跳房子的过程中，可以向前跳，也可以向后跳。

假设房子的总格数是count，小红每回合可能连续跳的步教都放在数组steps中，请问数组中是否有一种步数的组合，可以让小红两个回合跳到量后一格?如果有，请输出索引和最小的步数组合.

注意:

数组中的步数可以重复，但数组中的元素不能重复使用

。提供的数据保证存在满足题目要求的组合，且索引和最小的步数组合是唯一的

输入描述

第一行输入为房子总格数count，它是int整数类型。

第二行输入为每回合可能连续跳的步数，它是int整数数组类型

输出描述

返回索引和最小的满足要求的步数组合(顺序保持steps中原有顺序

备注

count ≤ 1000

0 ≤ steps.length ≤ 5000

-100000000 ≤steps ≤ 100000000



示例1：

输入

[1,4,5,2,2]

7



输出

[5, 2]

示例2：

输入

[-1,2,4,9,6]

8

输出

[-1, 9]

说明

此样例有多种组合满足两回合跳到最后，譬如: [-1,9]，[2,6]，其中[-1,9]的索引和为0+3=3，[2,6]的索和为1+4=5，所以索引和最小的步数组合[-1,9]
"""

"""
没啥思路：就一个{val: idx}的map，遍历看是否符合题意，然后索引和就是权重，取权重最小的
"""
def main():
    nums_str = input()[1:-1]    # 去掉中括号
    target = int(input())
    num_list = list(map(int, nums_str.split(",")))
    num_idx_map = {}
    for idx, num in enumerate(num_list):
        if num in num_idx_map:  # num_idx_map只存最小
            continue
        num_idx_map[num] = idx

    min_idx_sum = float("inf")
    res = []
    length = len(num_list)
    for idx in range(length):
        idx = length - 1 - idx      # 从后往前找
        num = num_list[idx]
        num2 = target - num
        if num2 not in num_idx_map:
            continue
        # idx相等说明num2与num相等, 因为num_idx_map是从前往后，num是从后往前，idx相等时说明一定是同一个位置的数字
        if num_idx_map[num2] == idx:
            continue
        if min_idx_sum > idx + num_idx_map[num2]:
            res = [num2, num]   # 倒序遍历，为了保持原有顺序，所以这样
            min_idx_sum = idx + num_idx_map[num2]
    print(res)

main()
