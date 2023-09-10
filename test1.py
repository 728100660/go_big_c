class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        """思路：因为是无限大的，所以只要大于最小的t,所有的t都是可达的，求出min_t即可"""
        if (sx, sy) == (fx, fy):        # 处于同一个点, 可以出去又回来，只有t=1，出去了就回不来了
            if t==0 or t > 1:
                return True
            else:
                return False
        diff_x = abs(sx - fx)
        diff_y = abs(sy - fy)
        min_t = max(diff_x, diff_y)
        return t>=min_t



if __name__ == '__main__':
    oSolution = Solution()

    # oSolution.isReachableAtTime(1, 2,1,2,1)
    assert oSolution.isReachableAtTime(2, 4, 7, 7, 6) == True
    assert oSolution.isReachableAtTime(1,1,1,1,3) == True