"""
由于可以把一个数一分为二，所以整个数组可以全部变成 1。因此如果 nums 的元素和小于target，则无解，返回 −1。否则一定有解。

然后从低位到高位贪心：

如果 target 的第 i 位是 0，跳过。
如果 target 的第 i 位是 1，那么先看看所有 ≤2^i的元素和能否 ≥target&mask
其中 mask==2^{i+1}-1。
如果能，那么必然可以合并出 target&mask，无需操作（见 视频 中的证明）。
如果不能，那么就需要把一个更大的数（设它是 2^j）不断地一分为二，直到分解出 2^i为止。
注意分解完后，2^i,2^{i+1},2^{i+2}, ,2^{j-1}这些 2 的幂我们都有了。
所以后面 i+1,i+2,⋯,j−1这些比特位都无需判断了，可以直接从第 j 个比特位开始判断。
class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        cnt = Counter(nums)
        ans = s = i = 0
        while 1 << i <= target:
            s += cnt[1 << i] << i
            mask = (1 << (i + 1)) - 1
            i += 1
            if s >= target & mask:
                continue
            ans += 1  # 一定要找更大的数操作
            while cnt[1 << i] == 0:
                ans += 1  # 还没找到，继续找更大的数
                i += 1
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/minimum-operations-to-form-subsequence-with-target-sum/solutions/2413344/tan-xin-by-endlesscheng-immn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

示例 1：

输入：nums = [1,2,8], target = 7
输出：1
解释：第一次操作中，我们选择元素 nums[2] 。数组变为 nums = [1,2,4,4] 。
这时候，nums 包含子序列 [1,2,4] ，和为 7 。
无法通过更少的操作得到和为 7 的子序列。
示例 2：

输入：nums = [1,32,1,2], target = 12
输出：2
解释：第一次操作中，我们选择元素 nums[1] 。数组变为 nums = [1,1,2,16,16] 。
第二次操作中，我们选择元素 nums[3] 。数组变为 nums = [1,1,2,16,8,8] 。
这时候，nums 包含子序列 [1,1,2,8] ，和为 12 。
无法通过更少的操作得到和为 12 的子序列。
示例 3：

输入：nums = [1,32,1], target = 35
输出：-1
解释：无法得到和为 35 的子序列。
"""
from collections import Counter

"""
# 题目：https://leetcode.cn/problems/minimum-operations-to-form-subsequence-with-target-sum/description/

简述：给一个数组和target, 将数组中的数一分为二，使得存在子数组和为target，求最小分割次数，不存在则返回-1

target可以写成二进制，数组中的所有数也能写成二进制
target开始遍历，从右到左，找到第i位为1的值， 例如，10，第二位为1
此时只要数组中存在2**{i-1}的数，就一定能组成i位以下的数，
如果没有，就在数组中找高位j分解到i-1，
分解完之后，直到j-1位，都是符合要求的，例如，j=4, i = 2， 1000==>[100, 100] ==>[100, 10, 10]，你看，是不是中间的所有位数都存在了

之后继续如此
思路
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        count_map = {}  # {num, count} 数组中各个数出现的个数
        for num in nums:
            if num not in count_map:
                count_map[num] = 0
            count_map[num] += 1

        max_i = target.bit_length() - 1 # 最多可右移位数
        i = 0
        ans = 0 #操作次数
        while i<=max_i:
            if (target >> i) & 1:     # 第i位为1
                if count_map.get(1 << i, 0) > 0:  # 存在2**i的数
                    i += 1
                    continue
                while count_map.get(1 << i, 0) <= 0:   # 查找是否有比2**(i)大的数
                    # 每左移一次就相当于分解一次
                    ans += 1
                    i += 1
                # while 出来，对当前num进行分解操作,cnt-1
                count_map[1 << i] -= 1
            i += 1  ######

        return ans


if __name__ == '__main__':
    oSolute = Solution()
    assert oSolute.minOperations([1, 2, 8], 7) == 1
    assert oSolute.minOperations([1, 32, 1, 2], 12) == 2
    assert oSolute.minOperations([1, 32, 1], 35) == -1