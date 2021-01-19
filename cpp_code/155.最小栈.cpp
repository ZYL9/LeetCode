/*
 * @lc app=leetcode.cn id=155 lang=cpp
 *
 * [155] 最小栈
 */

// @lc code=start
class MinStack
{
public:
    stack<int> A, B;
    MinStack() {}
    void push(int x)
    {
        A.push(x);
        if (B.empty() || B.top() >= x)
            B.push(x);
    }
    void pop()
    {
        if (A.top() == B.top())
            B.pop();
        A.pop();
    }
    int top()
    {
        return A.top();
    }
    int getMin()
    {
        return B.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
// @lc code=end
