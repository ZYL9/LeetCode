#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#递归
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#         if l1.val <= l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2
#
# #普通循环
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dum = ListNode(0)
#         move = dum
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 move.next = l1
#                 l1 = l1.next
#             else:
#                 move.next = l2
#                 l2 = l2.next
#             move = move.next
#         move.next = l1 if l1 else l2
#         return dum.next
#
#
#
# 用异常抛出减少时间
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = rst = ListNode(None)  ## 新建节点和指针
        while True:
            try:
                while l1.val <= l2.val:  ## 若l1更小，`p.next`就指向l1,同时更新l1，p节点
                    p.next = l1
                    l1, p = l1.next, p.next
                while l1.val > l2.val:  ## 若l2更小，`p.next`就指向l2,同时更新l2，p节点
                    p.next = l2
                    l2, p = l2.next, p.next
            except:
                break  ## 发生异常时，一定l1/l2至少一个为None了
        p.next = l1 or l2  ## 接上不为None的节点
        return rst.next  ##返回新建指针


# @lc code=end
