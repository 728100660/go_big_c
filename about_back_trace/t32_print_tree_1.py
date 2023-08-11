"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。



例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]


提示：

节点总数 <= 1000
"""
import collections

"""
思路：一层一层的遍历，很容易想到广度优先算法，
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res_list = []
        node_list = [root]
        while node_list:
            cur_node = node_list.pop(0)
            # if cur_node is None:      # 直接在添加的时候判断，避免消耗无用内存
            #     continue
            if cur_node.left is not None:
                node_list.append(cur_node.left)
            if cur_node.right is not None:
                node_list.append(cur_node.right)
            res_list.append(cur_node.val)
        return res_list
