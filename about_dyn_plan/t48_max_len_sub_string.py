"""
剑指 Offer 48. 最长不含重复字符的子字符串
中等
612
相关企业
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。



示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        1. 初始数组
        2. 状态转移 第n个字符串的子串长度等于，第n-1个的长度加1或者上一个字符到当前的长度，  方程为: dp[n] = min(dp[n-1] + 1, n_idx-idx_map[n])，
        3. 返回结果为max(dp)
        4. 可以优化dp数组为 cur和pre两个int类型的变量
        # 报错记录
        忽略
        return值
        max_len 需要在没一个判断条件都更新
        char_idx_map.get(char, -1)的默认值为-1而不是0
        """
        char_idx_map = {}
        dp = []
        max_len = 0
        for idx, char in enumerate(s):
            if not dp:
                dp.append(1)
                char_idx_map[char] = idx
                max_len = 1
                continue
            dp.append(min(dp[idx-1] + 1, idx - char_idx_map.get(char, -1)))
            max_len = max(dp[idx], max_len)
            char_idx_map[char] = idx
        return max_len


if __name__ == '__main__':
    oSolute = Solution()
    assert oSolute.lengthOfLongestSubstring("abcabcbb") == 3
