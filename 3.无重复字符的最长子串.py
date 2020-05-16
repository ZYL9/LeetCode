#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = 0
        l, r = 0, 0
        for i, c in enumerate(s):
            if c not in s[l:r]:
                r += 1
            else:
                l += s[l:r].index(c) + 1
                r += 1
            max_length = max(r - l, max_length)
        return max_length if max_length != 0 else len(s)


# @lc code=end
