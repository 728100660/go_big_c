"""
题目描述
小明玩一个游戏。

系统发1+n张牌，每张牌上有一个整数。 第一张给小明，后n张按照发牌顺序排成连续的一行。
需要小明判断，后n张牌中，是否存在连续的若干张牌，其和可以整除小明手中牌上的数字。

输入描述
输入数据有多组，每组输入数据有两行，输入到文件结尾结束。

第一行有两个整数n和m，空格隔开。m代表发给小明牌上的数字。

第二行有n个数，代表后续发的n张牌上的数字，以空格隔开。

输出描述
对每组输入，如果存在满足条件的连续若干张牌，则输出1;否则，输出0。

备注

1≤n≤1000
1≤牌上的整数≤400000
输入的数组，不多于1000 用例确保输入都正确，不需要考虑非法情况。
样例
输入

6 7
2 12 6 3 5 5
10 11
1 1 1 1 1 1 1 1 1 1
输出

1
0
说明

两组输入。第一组小明牌的数字为7，再发了6张牌。第1、2两张牌教字和为
14，可以整除7，输出1，第二组小明牌的数字为11，
再发了10张牌，这10张牌数字和为10，无法整除11，输出0。
"""

"""
二分法
左边和对 m求余数+ 右边对m求余数 之和 可以整除7，就算当前存在 


其实是：前缀和
"""
#
#
# def device_res(cards, m, left, right):
#     if left == right:
#         res = cards[left] % m
#         return res
#     mid = (left + right) // 2
#     res = 0
#     if left <= mid:     # 确保不会越界
#         left_res = device_res(cards, m, left, mid)
#         res += left_res     # 将余数保存，到时候和右边结果相加即可
#         if left_res == 0:   # 存在可以整除
#             return 0        # 直接返回
#     if mid + 1 <= right:
#         right_res = device_res(cards, m, mid + 1, right)
#         res += right_res
#         if right_res == 0:
#             return 0
#     return res % m
#
#
# def main():
#     card_num, m = tuple(map(int, input().split(" ")))
#     cards = list(map(int, input().split(" ")))
#     if device_res(cards, m, 0, card_num-1) == 0:
#         print(1)
#     else:
#         print(0)
#
#
# while True:
#     try:
#         main()
#     except EOFError:
#         break
