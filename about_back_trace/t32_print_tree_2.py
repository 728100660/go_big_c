"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。



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
  [9,20],
  [15,7]
]
"""

"""
还可以优化：
next_level_node的长度是可以在遍历之前就能确定的，可以不适用两个数组，以节省内存空间
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        next_level_node = [root]        # 下一层的节点集合
        while next_level_node:
            node_queue = next_level_node
            next_level_node = []
            tmp_res = []
            while node_queue:
                cur_node = node_queue.pop(0)
                if cur_node.left is not None:
                    next_level_node.append(cur_node.left)
                if cur_node.right is not None:
                    next_level_node.append(cur_node.right)
                tmp_res.append(cur_node.val)
            res.append(tmp_res)
        return res