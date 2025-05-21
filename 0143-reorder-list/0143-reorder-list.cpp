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
        auto curr = head;
        vector<ListNode*> list;
        while(curr) {
            list.push_back(curr);
            curr = curr->next;
        }
        bool flag = true;
        ListNode *temp;
        int i = 0, j = list.size() - 1;
        while(i < j) {
            // cout << i << " " << j << endl;
            if(flag) {
                list[i]->next = list[j]; // 2->8 // 4->6
                i++; // 4
                flag = false;
            } else {
                list[j]->next = list[i]; // 8->4
                j--; // 6
                flag = true;
            }
        }
        if(flag) { list[j]->next = nullptr; }
        else { list[i]->next = nullptr; }
        // 2->8->4->6
    }
};

/* NOTES:
0->1->2->3->4

0->4->1->3->2
*/