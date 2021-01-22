/*
 * @lc app=leetcode.cn id=138 lang=cpp
 *
 * [138] 复制带随机指针的链表
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution
{
public:
    Node *copyRandomList(Node *head)
    {
        if (head == nullptr)
            return nullptr;
        Node *c = head;
        while (c != nullptr)
        {
            Node *tmp = new Node(c->val);
            tmp->next = c->next;
            c->next = tmp;
            c = tmp->next;
        }
        c = head;
        while (c != nullptr)
        {
            if (c->random != nullptr)
                c->next->random = c->random->next;
            c = c->next->next;
        }
        c = head->next;
        Node *p = head;
        Node *r = head->next;
        while (c->next != nullptr)
        {
            p->next = p->next->next;
            c->next = c->next->next;
            p = p->next;
            c = c->next;
        }
        p->next = nullptr;
        return r;
    }
};
// @lc code=end
