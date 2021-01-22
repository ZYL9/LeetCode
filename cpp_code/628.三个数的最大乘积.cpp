/*
 * @lc app=leetcode.cn id=628 lang=cpp
 *
 * [628] 三个数的最大乘积
 */

// @lc code=start
class Solution
{
public:
    int maximumProduct(vector<int> &nums)
    {
        int min1 = __INT_MAX__, min2 = __INT_MAX__;
        int max1 = -__INT_MAX__, max2 = -__INT_MAX__, max3 = -__INT_MAX__;
        for (int x : nums)
        {
            if (x < min1)
            {
                min2 = min1;
                min1 = x;
            }
            else if (x < min2)
            {
                min2 = x;
            }

            if (x > max1)
            {
                max3 = max2;
                max2 = max1;
                max1 = x;
            }
            else if (x > max2)
            {
                max3 = max2;
                max2 = x;
            }
            else if (x > max3)
                max3 = x;
        }
        return max(min1 * min2 * max1, max1 * max2 * max3);
    }
};
// @lc code=end
