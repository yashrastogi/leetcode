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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int total_size = 0;
        auto t1 = head;
        while(t1) { total_size++; t1=t1->next; }
        int pos = total_size - n;
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* next = nullptr;
        while(curr) {
            next = curr->next;
            if(pos-- == 0) {
                if(prev == nullptr) 
                    head = next;
                else if(next == nullptr) 
                    prev->next = nullptr;
                else 
                    prev->next = next;
            }
            prev = curr;
            curr = curr->next;
        }
        return head;
    }
};
