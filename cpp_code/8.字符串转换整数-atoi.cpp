/*
 * @lc app=leetcode.cn id=8 lang=cpp
 *
 * [8] 字符串转换整数 (atoi)
 */

// @lc code=start
class Solution
{
public:
    int myAtoi(string str)
    {
        int res = 0, bond = INT_MAX / 10;
        int i = 0, sign = 1;
        int len = str.size();
        if (len == 0)
            return 0;
        while (str[i] == ' ')
        {
            if (++i == len)
                return 0;
        }
        if (str[i] == '-')
        {
            sign = -1;
            i++;
        }
        else if (str[i] == '+')
            i++;

        for (int j = i; j < len; j++)
        {
            if (str[j] < '0' || str[j] > '9')
                break;
            if (res > bond || res == bond && str[j] > '7')
                return sign == 1 ? INT_MAX : INT_MIN;
            res = res * 10 + (str[j] - '0');
        }
        return sign * res;
    }
};
// @lc code=end
