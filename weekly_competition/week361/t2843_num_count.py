"""
https://leetcode.cn/problems/count-symmetric-integers/
2843. 统计对称整数的数目
提示
简单
7
相关企业
给你两个正整数 low 和 high 。

对于一个由 2 * n 位数字组成的整数 x ，如果其前 n 位数字之和与后 n 位数字之和相等，则认为这个数字是一个对称整数。

返回在 [low, high] 范围内的 对称整数的数目 。



示例 1：

输入：low = 1, high = 100
输出：9
解释：在 1 到 100 范围内共有 9 个对称整数：11、22、33、44、55、66、77、88 和 99 。
示例 2：

输入：low = 1200, high = 1230
输出：4
解释：在 1200 到 1230 范围内共有 4 个对称整数：1203、1212、1221 和 1230 。

提示：

1 <= low <= high <= 10**4
"""
"""
思路：直接枚举+模拟
数据量很小，枚举没问题
"""
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high + 1):    # 遍历数组
            if self.is_half(num):
                ans += 1
        return ans


    def is_half(self, num):
        num_str = str(num)
        num_len = len(num_str)
        if num_len % 2 != 0:   # 非偶数个数组成的数
            return False
        left_sum = 0
        for idx in range(num_len // 2):
            left_sum += int(num_str[idx])
        right_sum = 0
        for idx in range(num_len//2, num_len):
            right_sum += int(num_str[idx])
        return left_sum == right_sum


if __name__ == '__main__':
    oSolute = Solution()
    assert oSolute.countSymmetricIntegers(1, 100) == 9
    assert oSolute.countSymmetricIntegers(1200, 1230) == 4