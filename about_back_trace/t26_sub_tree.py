"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3

    / \

   4   5

  / \

 1   2
给定的树 B：

   4

  /

 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None or B is None:
            return False
        if self.isPartEqual(A, B):
            return True
        # 从当前节点出发，没有找到子树，那就继续往下找
        left = self.isSubStructure(A.left, B)
        right = self.isSubStructure(A.right, B)
        return any([left, right])

    def isPartEqual(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:       # 只判断部分相等，b可以提前结束
            return True
        if A is None:
            return False
        if A.val != B.val:
            return False
        return self.isPartEqual(A.left, B.left) and self.isPartEqual(A.right, B.right)

