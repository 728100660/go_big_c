"""
剑指 Offer 13. 机器人的运动范围
中等
656
相关企业
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？



示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
"""

"""
注意，机器人只能从0出发，而且中间不能有断层，所以不能直接for循环计算mn的值
需要使用bfs
"""

class Solution:
    def __init__(self):
        self.total_count = 0

    def movingCount(self, m: int, n: int, k: int) -> int:
        total_count = 0
        flag_map = [[0 for _ in range(n)] for _ in range(m)]
        if not flag_map:
            return
        self.dfs(flag_map, 0, 0, k)
        return self.total_count

    def dfs(self, flag_map, i, j, k):
        if i < 0 or i >= len(flag_map):
            return
        if j < 0 or j >= len(flag_map[0]):
            return
        if flag_map[i][j] == 1:     # 该节点已经被访问过了
            return
        if not self.can_in(i, j, k):
            return
        self.total_count += 1
        flag_map[i][j] = 1  # 标记为已访问，不需要取消标记
        self.dfs(flag_map, i + 1, j, k)
        self.dfs(flag_map, i - 1, j, k)
        self.dfs(flag_map, i, j + 1, k)
        self.dfs(flag_map, i, j - 1, k)

    def can_in(self, i, j, k):
        sum = 0
        tmp_j = j
        while tmp_j // 10 != 0:
            sum += tmp_j % 10
            tmp_j = tmp_j // 10
        sum += tmp_j % 10
        tmp_i = i
        while tmp_i // 10 != 0:
            sum += tmp_i % 10
            tmp_i = tmp_i // 10
        sum += tmp_i % 10
        if sum <= k:
            return True
        return False


if __name__ == '__main__':
    oSolute = Solution()
    assert oSolute.movingCount(16, 8, 4) == 15