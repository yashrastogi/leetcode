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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0)
            return nullptr;
        priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>,
                       greater<>>
            heap;
        for (auto list : lists)
            if (list)
                heap.push({list->val, list});
        ListNode* head = new ListNode(-1001);
        auto curr = head;
        while (!heap.empty()) {
            auto [value, listhead] = heap.top();
            heap.pop();
            curr->next = new ListNode(value);
            curr = curr->next;
            if (listhead->next) {
                heap.push({listhead->next->val, listhead->next});
            }
            // delete (listhead);
        }
        return head->next;
    }
};