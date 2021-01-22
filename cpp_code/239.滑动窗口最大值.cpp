/*
 * @lc app=leetcode.cn id=239 lang=cpp
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
class Solution
{
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k)
    {
        int len = nums.size();
        vector<int> res(len - k + 1);
        deque<int> q;
        if (len == 0 || k == 0)
            return res;
        for (int i = 0; i < k; i++)
        {
            while (!q.empty() && q.back() < nums[i])
                q.pop_back();
            q.push_back(nums[i]);
        }
        res[0] = q.front();
        for (int i = k; i < len; i++)
        {
            if (q.front() == nums[i - k])
                q.pop_front();
            while (!q.empty() && q.back() < nums[i])
                q.pop_back();
            q.push_back(nums[i]);
            res[i - k + 1] = q.front();
        }
        return res;
    };
};
// @lc code=end
