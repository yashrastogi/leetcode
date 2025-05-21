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

class Solution {
public:
    void reorderList(ListNode* head) {
        if (head->next == nullptr)
            return;
        auto slow = head, fast = head, prev_slow = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }
        prev_slow->next = nullptr;
        auto curr = slow;
        ListNode* prev = nullptr;
        ListNode* temp = nullptr;
        while (curr) {
            temp = curr->next; // 8, temp=null
            curr->next = prev; // 6->null, 8->6
            prev = curr;       // prev=6, prev=8
            curr = temp;       // curr=8, curr=null
        }
        // prev is start of reversed half
        bool flag = true;
        auto second = prev, first = head;
        while (first && second) {
            if (flag) {
                temp = first->next;
                first->next = second;
                first = temp;
                flag = false;
            } else {
                temp = second->next;
                second->next = first;
                second = temp;
                flag = true;
            }
        }
    }
};

/* NOTES:
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 5, 4, 3]
[0->5->1->2->4->2->3]
*/