"""
https://leetcode.cn/problems/minimum-degree-of-a-connected-trio-in-a-graph/
一个图中连通三元组的最小度数
给你一个无向图，整数 n 表示图中节点的数目，edges 数组表示图中的边，其中 edges[i] = [ui, vi] ，表示 ui 和 vi 之间有一条无向边。

一个 连通三元组 指的是 三个 节点组成的集合且这三个点之间 两两 有边。

连通三元组的度数 是所有满足此条件的边的数目：一个顶点在这个三元组内，而另一个顶点不在这个三元组内。

请你返回所有连通三元组中度数的 最小值 ，如果图中没有连通三元组，那么返回 -1 。



示例 1：


输入：n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
输出：3
解释：只有一个三元组 [1,2,3] 。构成度数的边在上图中已被加粗。
示例 2：


输入：n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
输出：0
解释：有 3 个三元组：
1) [1,4,3]，度数为 0 。
2) [2,5,6]，度数为 2 。
3) [5,6,7]，度数为 2 。


n=6, edges=[[6,5],[4,3],[5,1],[1,4],[2,3],[4,5],[2,6],[1,3]]
res = 3


提示：

2 <= n <= 400
edges[i].length == 2
1 <= edges.length <= n * (n-1) / 2
1 <= ui, vi <= n
ui != vi
图中没有重复的边。
"""

"""
思路：dfs
1：构建一个路径map {v1: [v...]}  key是节点，val是该节点可达节点列表
2：dfs找到所有三元组
3：判断三元组的°
"""
from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # 构建一个路径map
        path_map = {}       # {v1: {v2, v3, v4}}
        for edge in edges:
            v1, v2 = edge
            path_map.setdefault(v1, set()).add(v2)
            path_map.setdefault(v2, set()).add(v1)

        # dfs遍历找到三元组
        tuple_3_list = set()     # {{v1,v2,v3}, {v4,v5,v6}}
        for head_node in path_map:
            path = {head_node}
            self.dfs(head_node, head_node, path, tuple_3_list, path_map, 1)

        if not tuple_3_list:
            return -1

        ans = 0
        du_list = []    # 所有三元组度的边集合 [(v1, v2)]
        # 判断三元组的度
        for tuple_3 in tuple_3_list:
            tuple_3 = set(tuple_3)
            for node in tuple_3:
                node_paths = path_map.get(node)
                next_nodes = node_paths - tuple_3      # 当前节点的度，所有可达节点减去所有三元组节点
                du_list.extend([(node, next_node) for next_node in next_nodes])
        # 清理在同一个三元组内的边
        for v1, v2 in du_list:
            correct = 1
            for tuple_3 in tuple_3_list:
                if v1 in tuple_3 and v2 in tuple_3: # 在同一个三元组内，不算度
                    correct = 0
                    break
            if correct:
                ans += 1
        return ans


    def dfs(self, head, this_node, path, tuple_3_list, path_map, num=1):
        if num == 3:
            next_node_list = path_map.get(this_node, set())
            if len(path) == 3 and head in next_node_list:      # 能指向头结点，形成三元组
                tuple_3_list.add(tuple(sorted(path)))   # 排序以达到去重目的
            return
        next_node_list = path_map.get(this_node, set())
        for next_node in next_node_list:
            tmp_path = path.copy()
            tmp_path.add(next_node)
            self.dfs(head, next_node, tmp_path, tuple_3_list, path_map, num + 1)


if __name__ == '__main__':
    oSolution = Solution()
    assert oSolution.minTrioDegree(6, [[6,5],[4,3],[5,1],[1,4],[2,3],[4,5],[2,6],[1,3]]) == 3
    assert oSolution.minTrioDegree(7, [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]) == 0
    assert oSolution.minTrioDegree(6, [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]) == 3
