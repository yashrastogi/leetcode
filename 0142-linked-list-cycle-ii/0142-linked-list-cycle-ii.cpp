/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* detectCycle(ListNode* head) {
        if (!head || !head->next)
            return nullptr;

        auto slow = head;
        auto fast = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            if (slow == fast)
                break;
        }
        if (slow != fast)
            return nullptr;
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        return fast;
    }
};
/*
           |    \/
 3 -> 0 -> 2 -> -4 -> 0 -> 2
 3 -> 2 -> 0 -> -4 -> 2 -> -4
           \/
 1 -> 1 -> 1 -> 1
 1 -> 2 -> 1 -> 2


*/