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

思路2：思路1是错误的，当图形为凹形的时候就不适用了，周长为最外边格子周长之和
适用bfs
return 上下左右相加
退出条件
当前值为0：return 1 
当前值被访问过且不为0：return 0

可能的边界条件：只有一个格子
"""


def dfs(grid, flag_grid, target, i, j):
    # 越界判断
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
        return 1
    if grid[i][j] != target:    # 到边界了
        return 1
    if flag_grid[i][j] == 1:    # 周围有已访问过格子
        return 0
    flag_grid[i][j] = 1     # 标记访问
    offset_list = ((0, 1), (0, -1), (1, 0), (-1, 0))
    res = 0
    for offset_i, offset_j in offset_list:
        res += dfs(grid, flag_grid, target, i+offset_i, j+offset_j)
    return res



def main():
    graph_num = int(input())
    res = []
    grid = [[0] * 64 for _ in range(64)]
    flag_grid = [[0] * 64 for _ in range(64)]   # 访问标记地图
    # 初始化矩阵
    for _ in range(graph_num):
        graph_info = list(map(int, input().split(" ")))
        fill_num = graph_info[0]    # 填充数字
        idx = 1
        while idx < len(graph_info):
            i = graph_info[idx]
            j = graph_info[idx+1]
            grid[i][j] = fill_num
            idx += 2
        res.append(dfs(grid, flag_grid, fill_num, graph_info[1], graph_info[2]))

    for total in res:
        print(total, end=" ")


main()
