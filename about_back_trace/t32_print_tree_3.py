"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
"""
import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        node_queue = collections.deque()
        node_queue.append(root)
        reverse = 1    # -1表示反转， 1不反转
        while node_queue:
            tmp_res = []
            for _ in range(len(node_queue)):
                cur_node = node_queue.popleft()
                tmp_res.append(cur_node.val)
                if cur_node.left:
                    node_queue.append(cur_node.left)
                if cur_node.right:
                    node_queue.append(cur_node.right)
            if reverse == -1:
                res.append(tmp_res[::-1])
            else:
                res.append(tmp_res)
            reverse *= -1
        return res