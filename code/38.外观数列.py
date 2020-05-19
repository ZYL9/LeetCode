#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if (n == 1):
            return '1'
        num = self.countAndSay(n - 1) + "*"
        temp = list(num)
        count = 1
        strBulider = ''
        for i in range(len(temp) - 1):
            if temp[i] == temp[i + 1]:
                count += 1
            else:
                strBulider += str(count) + temp[i]
                count = 1
        return strBulider


#这个题递归效率比动态规划要高

# @lc code=end
