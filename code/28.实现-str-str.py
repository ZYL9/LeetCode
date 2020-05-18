#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 无敌取巧1
        # return haystack.index(needle) if needle in haystack else -1
        # 无敌取巧2
        # 效率比1高！find函数很强
        # return haystack.find(needle)

        #正经做法 效率是最高的！时间复杂度是O(n)
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


# @lc code=end
