"""
题目描述
有一名科学家想要从一台古董电脑中拷贝文件到自己的电脑中加以研究

但此电脑除了有一个
3.5寸软盘驱动器以外，没有任何手段可以将文件持贝出来，而且只有一张软盘可以使用。

因此这一张软盘是唯一可以用来拷贝文件的载体。

科学家想要尽可能多地将计算机中的信息拷贝到软盘中，做到软盘中文件内容总大小最大。
已知该软盘容量为1474560字节。文件占用的软盘空间都是按块分配的，每个块大小为512个字节。

一个块只能被一个文件使用。拷贝到软盘中的文件必须是完整的，且不能采取任何压缩技术。

输入描述
第1行为一个整数N，表示计算机中的文件数量。
1≤N≤1000

接下来的第2行到第N+1行(共N行)，每行为一个整数，表示每个文件的大小Si，单位为字节。

O≤i≤N,
0≤Si

输出描述
科学家最多能拷贝的文件总大小

备注

为了充分利用软盘空间，将每个文件在软盘上占用的块记录到本子上。即真正占用软盘空间的只有文件内容本身。

样例
输入

3
737270
737272
737288
输出

1474542
说明

3
3个文件中，每个文件实际占用的大小分别为
737280字节、
737280字节、
737792字节.只能选取前两个文件，总大小为
1474542字节。

虽然后两个文件总大小更大且未超过
1474560字节，但因为实际占用的大小超过了
1474560字节，所以不能选后两个文件。

输入

6
400000
200000
200000
200000
400000
400000
输出

1400000
说明

从
6个文件中，选择
3个大小为
400000的文件和
1个大小为
200000的文件，得到最大总大小为
1400000。

也可以选择
2个大小为
400000的文件和
3个大小为
200000的文件，得到的总大小也是
1400000。
"""

"""
本质就是01背包问题
dp[i][j] 表示的就是第i个物品，背包承重为j的价值

状态转移： dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + val[i])
dp[i-1][j-weight[i]] + val[i]： 对于当前的i, j来说, 上一个物品的价值就是 dp[i-1][j-weight[i]]

注意事项：
1. 遍历应该从1开始，而不是从0开始，dp数组要比原列表长度大1
2. 背包空间不足应该是j < weight 而不是<= 
优化后
3. 优化后第一层for循环不需要+1了，所以内层判断不需要判断i是否为0的情况了
4. j = 0时，weight = 0， val也等于0， cur_dp[j] = cur_dp[j]啥也没变，所以没必要写
"""


def main():
    file_num = int(input())
    if file_num == 0:
        return 0
    file_size_list = []
    for _ in range(file_num):
        file_size_list.append(int(input()))

    bucket_num = 1474560 // 512  # 这俩相除不会有小数点，= 2880
    cur_dp = [0] * (bucket_num + 1)
    for i in range(file_num):
        pre_dp = cur_dp
        weight = (file_size_list[i] + 511) // 512  # 重量
        val = file_size_list[i]  # 价值
        for j in range(bucket_num, weight - 1, -1):  # 因为是同一个数组，从后往前走防止重复拿文件
            cur_dp[j] = max(pre_dp[j], pre_dp[j - weight] + val)
    return cur_dp[bucket_num]


print(main())

#
# # 非优化版本：
# def main2():
#     import math
#     file_num = int(input())
#     if file_num == 0:
#         return 0
#     file_size_list = []
#     for _ in range(file_num):
#         file_size_list.append(int(input()))
#
#     bucket_num = 1474560 // 512    # 这俩相除不会有小数点，= 2880
#     dp = [[0] * (bucket_num + 1) for _ in range(file_num + 1)]
#     for i in range(file_num + 1):
#         for j in range(bucket_num + 1):
#             if i == 0 or j == 0:        # 没有物品可选，和 背包承重为0，则都为0
#                 continue
#             # 因为i目前代表的是第i个物品，第i个物品的下标为i-1
#             weight = math.ceil(file_size_list[i-1] / 512) # 重量
#             val = file_size_list[i-1] # 价值
#             if j < weight:     # 背包空间不足，放不下当前物品
#                 dp[i][j] = dp[i - 1][j]
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + val)
#     return dp[file_num][bucket_num]
#
# print(main2())
