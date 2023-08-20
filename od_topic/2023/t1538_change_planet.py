"""
行星改造计划

题目描述
2XXX年，人类通过对火星的大气进行宜居改造分析，使得火星已在理论上具备人类宜居的条件;

由于技术原因，无法一次性将火星大气全部改造，只能通过局部处理形式;

假设将火星待改造的区域为
row∗column的网格，每个网格有
3个值，宜居区、可改造区、死亡区，使用
YES、
NO、
NA代替，
YES表示该网格已经完成大气改造，
NO表示该网格未进行改造，后期可进行改造，
NA表示死亡区，不作为判断是否改造完的宜居，无法穿过;

初始化下，该区域可能存在多个宜居区，并目每个宜居区能同时在每个大阳日单位向上下左右四个方向的相邻格子进行扩散，自动将
4个方向相邻的真空区改造成宜居区:

请计算这个待改造区域的网格中，可改造区是否能全部成宜居区，如果可以，则返回改造的大阳日天教，不可以则返回
−1

输入描述
输入
row∗column个网格数据，每个网格值枚举值如下:
YES，
NO，
NA;

样例:
YES YES NO
NO NO NO
NA NO YES

输出描述
可改造区是否能全部变成宜居区，如果可以，则返回改造的太阳日天数，不可以则返回−1。

备注
grid[i][j]只有3种情况，YES、NO、NA

row == grid.length
column == grid[i].length
1≤row, column≤8
样例
输入

YES YES NO
NO NO NO
YES NO NO
输出

2
说明

进过2个太阳日，完成宜居改造。

输入

YES NO NO NO
NO NO NO NO
NO NO NO NO
NO NO NO NO
输出

6
说明

经过
6
6个太阳日，可完成改造。

输入

NO NA
输出

-1
说明

无改造初始条件，无法进行改造。

输入

YES NO NO YES
NO NO YES NO
NO YES NA NA
YES NO NA NO
输出

-1
说明

−
1
−1//右下角的区域，被周边三个死亡区挡住，无法实现改造。
"""


"""
思路：bfs，dfs都可以，因为这里是扩散的，所以和bfs的思想非常相似，使用bfs就很好理解

离谱的not ac，写出代码之后死活通过不了，照着答案意思写都不对
最后发现是 split() 和 split(" ")的区别，我是用的第二个split  

split会寻找连续的空格作为分隔符
"""


def dfs(grid, visit_grid, i, j, can_tans=1):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return 0
    if visit_grid[i][j] == 1:
        return 0
    if grid[i][j] == "NA":
        return -1
    if grid[i][j] == "NO":      # 改造，并且返回，一天只能改造一次
        if can_tans:        # 只有由其他yes过来的才能trans，第一次调用的时候tans都为0
            visit_grid[i][j] = 1
            grid[i][j] = "YES"
            return 1
        return 0
    visit_grid[i][j] = 1
    grid[i][j] = "YES"
    next_grid_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    total_num = 1
    for x, y in next_grid_list:
        num = dfs(grid, visit_grid, i+x, j+y)
        if num == -1:
            return -1
        total_num += num
    return total_num


def main():
    grid = []
    # 输入获取
    while True:
        try:
            tmp_list = input().split()
            # if "-" in tmp_list:
            #     raise Exception
            grid.append(tmp_list)
        except Exception as e:
            break
    row = len(grid)
    col = len(grid[0])

    # 记录可改造区数量
    need_change = 0
    # 记录宜居区坐标位置
    queue = []
    # 初始化
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "YES":     # 宜居区，可扩散
                queue.append((i, j))
            elif grid[i][j] == "NO":     # 待改造
                need_change += 1

    if not queue:    # 没有宜居区
        return -1
    elif len(queue) == row * col:  # 全是宜居区
        return 0

    # 上下左右四个方向的偏移量
    next_grid_list = ((-1, 0), (1, 0), (0, -1), (0, 1))

    day = 0     # 每天向外扩散一圈，并记录扩散的数量，等于待改造总数即全部改造完毕
    while queue and need_change > 0:
        next_queue = []     # 下一天应该扩散的坐标
        for i, j in queue:    # 一天的向外扩散
            for offset_i, offset_j in next_grid_list:
                new_i = i + offset_i
                new_j = j + offset_j
                if not (0 <= new_i < row and 0 <= new_j < col):  # 判断越界
                    continue
                if grid[new_i][new_j] == "NO":  # 周围为NO，加入下一天的扩散计划，并且标记为YES
                    next_queue.append([new_i, new_j])
                    grid[new_i][new_j] = "YES"
                    need_change -= 1

        day += 1
        queue = next_queue

    if need_change == 0:
        return day
    return -1


print(main())
