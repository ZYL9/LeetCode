#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        # 做代数转换 理论上效率是最高的
        # ans = int(math.exp(0.5 * math.log(x)))
        # return ans + 1 if (ans + 1)**2 <= x else ans

        #牛顿迭代
        a, b = float(x), float(x)
        while True:
            xi = 0.5 * (a + b / a)
            if abs(a - xi) < 1e-7:
                break
            a = xi
        return int(a)


# @lc code=end
