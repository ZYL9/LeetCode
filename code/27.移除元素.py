#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #取巧做法
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        #
        #双指针
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


#难过的是两种方法效率基本一样，日后用到不如取巧的方法

# @lc code=end
