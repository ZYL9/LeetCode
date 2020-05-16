#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        for i in range(0, len(x) // 2):
            if x[i] != x[len(x) - i - 1]:
                return False
        return True


# @lc code=end
