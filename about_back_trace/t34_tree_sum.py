"""
剑指 Offer 34. 二叉树中和为某一值的路径
中等
442
相关企业
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。



示例 1：



输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
示例 2：



输入：root = [1,2,3], targetSum = 5
输出：[]
示例 3：

输入：root = [1,2], targetSum = 0
输出：[]


提示：

树中节点总数在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.dfs(root, target, [], res)
        return res

    def dfs(self, root, target, path_list, res_list):
        """深度查找是否和为target的节点"""
        # 这种方法会导致叶子结点判断两次
        # if target < 0:
        #     return False
        # if not root:    # 叶子结点
        #     if target == 0:
        #         res_list.append(path_list)
        #         return True
        #     return False
        # path_list.append(root.val)
        # self.dfs(root.left, target - root.val, path_list.copy(), res_list)
        # self.dfs(root.right, target - root.val, path_list.copy(), res_list)
        if not root:
            return False
        path_list.append(root.val)
        if root.left is None and root.right is None:
            if root.val == target:
                res_list.append(path_list)
                return True
        if root.left:
            self.dfs(root.left, target - root.val, path_list.copy(), res_list)
        if root.right:
            self.dfs(root.right, target - root.val, path_list.copy(), res_list)
