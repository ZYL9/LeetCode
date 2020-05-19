#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        amax = nums[0]
        asum = nums[0]
        for i in nums[1:]:
            asum = asum + i if asum >= 0 else i
            amax = amax if amax > asum else asum
        return amax


# @lc code=end
