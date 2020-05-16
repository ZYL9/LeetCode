#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        r2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        Int = 0
        for i in range(n - 1):
            if r2i[s[i]] < r2i[s[i + 1]]:
                Int -= r2i[s[i]]
            else:
                Int += r2i[s[i]]
        return Int + r2i[s[-1]]


# @lc code=end
