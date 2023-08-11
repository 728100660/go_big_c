"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。





示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
"""
from typing import List

"""
这个题看起来就是26题子树的进阶版，26题思路应该有点错
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                target_idx = 0
                if self.dfs(board, word, i, j, target_idx):
                    return True
        return False

    def dfs(self, board: List[List[str]], word: str, i, j, target_idx) -> bool:
        # 边界判断
        if target_idx >= len(word):
            return True
        if i < 0 or i >= len(board):
            return False
        if j < 0 or j >= len(board[0]):     # board必不为空，开始就判断了
            return False
        # 值判断
        cur_val = board[i][j]   # 暂时保存当前值
        if cur_val != word[target_idx]:
            return False
        board[i][j] = " "     # 修改值，避免重复访问
        if self.dfs(board, word, i-1, j, target_idx + 1):
            board[i][j] = cur_val   # 还原
            return True
        if self.dfs(board, word, i+1, j, target_idx + 1):
            board[i][j] = cur_val   # 还原
            return True
        if self.dfs(board, word, i, j-1, target_idx + 1):
            board[i][j] = cur_val   # 还原
            return True
        if self.dfs(board, word, i, j+1, target_idx + 1):
            board[i][j] = cur_val   # 还原
            return True   # 还原
        board[i][j] = cur_val   # 还原
        return False

if __name__ == '__main__':
    oSolute = Solution()
    assert oSolute.exist([["A","A"],["B","C"]], "AAB") == True