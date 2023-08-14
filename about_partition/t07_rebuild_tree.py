"""
剑指 Offer 07. 重建二叉树
中等
1.1K
相关企业
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。



示例 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
示例 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


限制：

0 <= 节点个数 <= 5000
"""
from typing import List


"""
# 前序[mid, left, right]  中序遍历[left, mid, right]
# 前序的每个节点都是中间节点   前序的后一个节点在中序相对mid节点的位置，可以判断是left还是right

正确思路：分治
## 前序节点每一个都是root节点，遍历前序数组，将中序遍历数组分割成left，和right两个部分一直下去直到只剩下一个节点
错点
## 递归结束条件判断
## 确保每次使用前序节点的时候都使得idx+1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        def get_mid_node(left_idx, right_idx):
            if not 0 <= left_idx <= right_idx < len(inorder):    # 边界不符合条件
                return None
            mid_node = TreeNode(preorder[self.mid])
            mid_idx = inor_idx_map.get(mid_node.val)
            if mid_idx < left_idx or mid_idx > right_idx:      # 根节点不在区间范围内
                return None
            self.mid += 1   # 每轮用完后节点指向下一个
            left_node = get_mid_node(left_idx, mid_idx-1)
            right_node = get_mid_node(mid_idx+1, right_idx)
            mid_node.left = left_node
            mid_node.right = right_node
            return mid_node

        inor_idx_map = {val: idx for idx, val in enumerate(inorder)}
        self.mid = 0        # 记录根节点下标
        head = get_mid_node(0, len(inorder)-1)
        return head

if __name__ == '__main__':
    oSolute = Solution()
    assert oSolute.buildTree([3,9,20,15,7], [9,3,15,20,7]) == True

