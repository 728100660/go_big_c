"""
题目内容
AI识别到面板上有  (1≤N≤100) 个指示灯，灯大小一样，任意两个之间无重叠。

由于AI识别误差，每次识别到的指示灯位置可能有差异，以4个坐标值描述AI识别的指示灯的大小和位置(左上角 x1, y1，右下角   x2,y2)

请输出先行后列排序的指示灯的编号，排序规则:

1.每次在尚未排序的灯中挑选最高的灯作为的基准灯，

2.找出和基准灯属于同一行所有的灯进行排序。两人灯高低偏差不超过灯半径算同一行(即两个灯坐标的差≤灯高度的一半)。

输入描述
第一行为
N，表示灯的个数 接下来N行，每行为
1个灯的坐标信息，格式为:

编号x_1 y_1 x_2 y_2
编号全局唯一
1≤编号≤100
1<=x1<x2<=1000
1<=y1<y2<=1000
输出描述
排序后的编号列表，编号之间以空格分隔

用例
输入

5
1 0 0 2 2
2 6 1 8 3
3 3 2 5 4
5 5 4 7 6
4 0 4 2 6
输出

1 2 3 4 5
"""


"""
思路：没有思路，题目都看不懂
姑且假装ai识别的是对的吧
1 建立一个中间map  {row: [(), (), ()]}  按照行，对同行及符合要求的灯进行排序，排序完之后就删除对应元素
太复杂了，尽量建立数据结构来简化代码

注意，x, y 表示的是grid[y][x]处的元素
"""
class CNode(object):
    def __init__(self, num, x1, y1, x2, y2):
        self.num = num
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def main():
    light_num = int(input())

    node_list = []
    for _ in range(light_num):
        light_infos = list(map(int, input().split(" ")))
        oNode = CNode(*light_infos)
        node_list.append(oNode)

    node_list.sort(key=lambda x: x.y1)
    start = 0
    for i in range(len(node_list)):
        if node_list[i].y1 - node_list[start].y1 <= (node_list[start].y2 - node_list[start].y1) / 2:
            continue
        node_list[start:i] = sorted(node_list[start:i], key= lambda x: x.x1)
        start = i

    node_list[start:] = sorted(node_list[start:], key=lambda x: x.x1)

    for nod in node_list:
        print(nod.num, end=" ")


main()
