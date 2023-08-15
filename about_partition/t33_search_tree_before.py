"""
剑指 Offer 33. 二叉搜索树的后序遍历序列
中等
748
相关企业
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

示例 1:

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
"""

"""
后序[left, right, root]     left < root < right
分治法：
1. 找到root节点
2. 按照root分割
3. 难点-判断区间内为二叉树：后序遍历的特性，list[-1]一定为root节点，并且由后序的特性可知，
   数组一定划分为两个连续的部分，左边部分全部小于root，右边部分全部大于root; 
   当按照root分割的左右区间都满足规则且当前区间满足规则，则证明当前区间内是搜索二叉树
"""


class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(left_idx, right_idx):
            left_val = postorder[left_idx]
            if postorder[left_idx + 2] < postorder[left_idx + 1]:   # 说明 +1 是右节点，+2是父节点
                m = left_idx + 2
            else:
                m = left_idx + 1