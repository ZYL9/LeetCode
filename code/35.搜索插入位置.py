#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 提前判断提高效率
        if target > nums[-1]:
            return len(nums)

        # 最朴素的遍历 时间复杂度O(n)
        j = 0
        for i in range(0, len(nums)):
            if nums[i] < target:
                j += 1
            else:
                return j
        # return j 不如提前判断

        # 二分法 竟然更慢了 惊了
        # l, r = 0, len(nums) - 1
        # ans = -1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] >= target:
        #         r = mid - 1
        #         ans = mid
        #     else:
        #         l = mid + 1
        # return ans


# @lc code=end
