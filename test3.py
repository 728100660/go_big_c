from typing import List


class Solution:
    # def minimumMoves(self, grid: List[List[int]]) -> int:
    #     """思路，因为元素之和为9，所以，>1的石头肯定是要分出去的，>1开始广度优先，把石头分出去"""
    #     move_count = 0
    #     for i in range(3):
    #         for j in range(3):
    #             while grid[i][j] > 1:
    #                 move_count += self.bfs(grid, i, j)
    #     return move_count
    #
    # def bfs(self, grid, i, j):
    #     flag_map = [[0] * 3 for _ in range(3)]
    #     flag_map[i][j] = 1
    #     grid[i][j] -= 1  # 分1个石头出去
    #     my_queue = [(i, j)]
    #     move_count = 0
    #     diff_list = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # 方向列表
    #     while my_queue:
    #         new_queue = []
    #         move_count += 1  # 一定是能走一次的
    #         for pos in my_queue:  # 遍历一层
    #             ti, tj = pos
    #             for di, dj in diff_list:
    #                 new_i, new_j = ti + di, tj + dj
    #                 if new_i < 0 or new_i >= 3 or new_j < 0 or new_j >= 3 or flag_map[new_i][new_j] == 1:  # 判断边界
    #                     continue
    #                 if grid[new_i][new_j] == 0:
    #                     grid[new_i][new_j] = 1
    #                     return move_count  # 一定是能走到这里的
    #                 flag_map[new_i][new_j] = 1  # 标记不可访问
    #                 new_queue.append((new_i, new_j))
    #         my_queue = new_queue
    #     return move_count

    def minimumMoves(self, grid: List[List[int]]) -> int:
        """思路 bfs从0开始从旁边找一个>1的分给他"""
        move_count = 0
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    move_count += self.bfs(grid, i, j)
        return move_count

    def bfs(self, grid, i, j):
        flag_map = [[0] * 3 for _ in range(3)]
        flag_map[i][j] = 1
        my_queue = [(i, j)]
        move_count = 0
        diff_list = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # 方向列表
        while my_queue:     # 一次while就是走一层
            new_queue = []
            move_count += 1  # 一定是能走一次的
            for pos in my_queue:  # 遍历一层
                ti, tj = pos
                for di, dj in diff_list:
                    new_i, new_j = ti + di, tj + dj
                    if new_i < 0 or new_i >= 3 or new_j < 0 or new_j >= 3 or flag_map[new_i][new_j] == 1:  # 判断边界
                        continue
                    if grid[new_i][new_j] > 1:     # 有多余的石头，直接分
                        grid[new_i][new_j] -= 1
                        grid[i][j] = 1
                        return move_count  # 一定是能走到这里的
                    flag_map[new_i][new_j] = 1  # 标记不可访问
                    new_queue.append((new_i, new_j))
            my_queue = new_queue
        return move_count


[[1,1,0],[1,1,1],[1,2,1]]
[[1,3,0],[1,0,0],[1,0,3]]




if __name__ == '__main__':
    oSolution = Solution()
    """
    [3,2,0],
    [0,1,0],
    [0,3,0]
    """
    assert oSolution.minimumMoves([[3,2,0],[0,1,0],[0,3,0]]) == 4
    """
    [1,2,2],
    [1,1,0],
    [0,1,1]]
    """
    assert oSolution.minimumMoves([[1,2,2],[1,1,0],[0,1,1]]) == 4
    # assert oSolution.waysToBuyPensPencils(5, 10, 10) == 1
