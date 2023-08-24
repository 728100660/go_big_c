"""
MELON 难题
石头分配

题目描述
MELON有一堆精美的雨花石(数量为n，重量各异)，准备送给S和W。
MELON希望送给俩人的雨花石重量一致，请你设计一个程序，帮
MELON确认是否能将雨花石平均分配。

输入描述
第
1行输入为雨花石个数:
n，0<n<31。 第
2行输入为空格分割的各雨花石重量:
m[0]m[1].....m[n−1]，0<m[k]<1001 不需要考虑异常输入的情况

输出描述
如果可以均分，从当前雨花石中最少拿出几块，可以使两堆的重量相等;如果不能均分，则输出
−1。

样例
输入

4
1 1 2 2
输出

2
说明

输入第一行代表共4颗雨花石

第二行代表4颗雨花石重量分别为
1、1、2、2。

均分时只能分别为
1,2，需要拿出重量为
1和2的两块雨花石，所以输出2。

输入

10
1 1 1 1 1 9 8 3 7 10
输出

3
说明

输入第一行代表共10颗雨花石

第二行代表4颗雨花石重量分别为
1、1、1、1、1、9、8、3、7、10 。

均分时可以
1,1,1,1,1,9,7和
10,8,3，也可以
1,1,1,1,9,8和
10,7,3,1，或者其他均分方式，但第一种只需要拿出重量为
10,8,3的
3块雨花石，第二种需要拿出
4块，所以输出
3(块数最少)
"""


"""
dp[i][j]        表示第i个石头，重量为j 的最少拿石头个数

dp[i][j] = min(dp[i-1][j], dp[i-1][j-weight] + 1)
拿：上一个没达到要求重量的个数 + 1
不拿：上一个已达到要求重量的个数
取最小值

优化：
dp[j] = min(pre[j], pre[j-weight] + 1)

思路：动态规划
dp为重量j时刻的最少个数
要求均分：
所以重量和必须能整除2
得到均分重量weight
只要看dp[weight]有没有值就行，没有值就返回-1


"""


def main():
    """动态规划"""
    count = int(input())
    weight_list = list(map(int, input().split()))       # 石头重量数目
    sum_weight = sum(weight_list)
    if sum_weight % 2 != 0:
        return -1
    mid_weight = sum_weight // 2        # 范围在 (30 * 1000) / 2

    dp = [float("inf")] * (mid_weight + 1)
    dp[0] = 0       # 重量为0也算作一种方法
    for i in range(len(weight_list)):
        pre_dp = dp
        for j in range(mid_weight, 0, -1):
            weight = weight_list[i]
            if j < weight:
                continue
            dp[j] = min(pre_dp[j], pre_dp[j-weight] + 1)
    if dp[mid_weight] > 31:
        return -1
    return dp[mid_weight]


print(main())
