"""
相同数字组成图形的周长
题目描述
有一个
64x64的矩阵，每个元素的默认值为0，现在向里面填充数字，相同的数字组成一个实心图形，
如下图所示是矩阵的局部(空白表示填充0)
输入描述
第一行输入N，表示N个图形，
N>0且 N<64 x 64
矩阵左上角单元格坐标记作(0,0)，第一个数字表示行号，第二个数字表示列号
接下来是N行，每行第一个数是矩阵单元格填充的数字，后续每两个一组，表示填充该数字的单元格坐标
答题者无需考虑数据格式非法的场景，题目用例不考察数据格式
题目用例保证同一个填充值只会有一行输入数据
输出描述
一共输出N个数值，每个数值表示某一行输入表示图形的周长
输出顺序需和输入的隔行顺序保持一致，即第1个数是输入的第1个图形的周长，第2个数是输入的第2个图形的周长，以此类推。
输入

2
1 1 3 2 2 2 3 2 4 3 2 3 3 3 4 4 1 4 2 4 3 4 4 5 2 5 3
2 3 7 3 8 4 5 4 6 4 7 4 8 5 4 5 5 5 6 5 7 5 8 6 4 6 5 6 6 6 7 6 8 7 4 7 5 7 6 7 7 7 8
输出

18 20
说明

无
"""

"""
思路：因为是矩形，且连续图形，所以周长等于(max(x)-min(x) + max(y) - min(y)) * 2
"""


def main():
    graph_num = int(input())
    res = []
    for _ in range(graph_num):
        graph_info = list(map(int, input().split(" ")))
        idx = 1
        max_i, min_i = graph_info[1], graph_info[1]
        max_j, min_j = graph_info[2], graph_info[2]
        while idx < len(graph_info):
            i, j = graph_info[idx], graph_info[idx + 1]
            max_i = max(max_i, i)
            max_j = max(max_j, j)
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            idx += 2
        max_i = min(max_i, 63)
        max_j = min(max_j, 63)
        min_i = max(min_i, 0)
        min_j = max(min_j, 0)
        this_res = (max_i - min_i + 1 + max_j - min_j + 1) * 2
        res.append(this_res)

    for total in res:
        print(total, end=" ")


main()
