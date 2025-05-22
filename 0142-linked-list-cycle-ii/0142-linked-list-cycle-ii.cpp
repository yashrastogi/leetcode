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
    ListNode *detectCycle(ListNode *head) {
        set<ListNode *> seen;
        for(auto curr = head; curr; curr = curr->next) {
            if(seen.count(curr)) return curr;
            seen.insert(curr);
        }
        return nullptr;
    }
};