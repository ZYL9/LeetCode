/*
 * @lc app=leetcode.cn id=206 lang=cpp
 *
 * [206] 反转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *tmp = nullptr;
        ListNode *c = head;
        ListNode *p = nullptr;
        while (c != nullptr)
        {
            tmp = c->next;
            c->next = p;
            p = c;
            c = tmp;
        }
        return p;
    }
};
// @lc code=end
