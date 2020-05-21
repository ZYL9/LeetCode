#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # s = s.split()
        # return len(s[-1]) if s else 0

        s = s.rstrip()
        if s.count(' ') == 0:
            return len(s)
        x = 0
        while True:
            if s[-(x + 1)] == ' ':
                return x
            x += 1


# @lc code=end
