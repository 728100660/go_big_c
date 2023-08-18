"""
2023.05-B卷-华为OD机试 - 报文回路-”新加题型“（100分值）
题目描述
IGMP 协议中响应报文和查询报文，是维系组播通路的两个重要报文，在一条已经建立的组播通路中两个相邻的 HOST 和 ROUTER,
ROUTER 会给 HOST 发送查询报文，HOST 收到查询报文后给 ROUTER 回复一个响应报文，以维持相之间的关系，
一但存在非双向的关系，那么这条组播涌路就异常了。现通过某种手段，抓取到了
HOST和 ROUTER 两者通讯的所有响应报文和查询报文，请分析该组播通路是否“正常”

输入描述
第一行抓到的报文数量
C(C≤100)，后续C行依次输入设备节点
D1和D2，表示D1到D2可以发送单向的报文，
D1和D2用空格隔开

1≤D1   D2 < 1e9

输出描述
组播通路是否“正常”，正常输出True， 异常输出False。

样例
输入

5
1 2
2 3
3 2
1 2
2 1
输出

True
说明

无

输入

3
1 3
3 2
2 3
输出

False
说明

无
"""

"""
思路：还是用map ： arrive_map = {node: set()}       节点，以及对应节点的可达节点集合
先遍历，初始化  arrive_map
再遍历, 查看cur 是否在 arrive_map[cur.next]， 不在直接返回
"""
def main():
    msg_num = int(input())
    arrive_map = {}
    node_arrive_list = []       # [[node1, node2], [], []]
    for _ in range(msg_num):
        arrive_list = list(map(int, input().split(" ")))
        node1, node2 = arrive_list[0], arrive_list[1]
        node_arrive_list.append(arrive_list)
        if node1 not in arrive_map:
            arrive_map[node1] = set()
        arrive_map[node1].add(node2)

    for arrive_list in node_arrive_list:
        node1, node2 = arrive_list[0], arrive_list[1]
        if node2 not in arrive_map:   # 该节点不可达任何节点
            return False
        if node1 not in arrive_map.get(node2):      # 节点2不可达节点1
            return False
    return True


print(main())
