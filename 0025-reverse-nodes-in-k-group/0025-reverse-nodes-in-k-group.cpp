
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (k == 1)
            return head;
        int node_count = 0;
        for (auto curr = head; curr; curr = curr->next)
            node_count++;
        ListNode* returnHead = nullptr;
        ListNode* curr_head = head;
        ListNode* curr_head_prev = nullptr;
        ListNode* curr_tail = nullptr;
        ListNode* curr_tail_next = nullptr;
        bool firstTime = true;
        bool setHead = false;
        int count = 1;
        for (auto curr = head; curr; curr = curr->next) {
            if (count % k == 0) {
                curr_tail = curr;
                curr_tail_next = curr->next;
                // if (curr_head)
                //     cout << "CH: " << curr_head->val << " ";
                // if (curr_tail)
                //     cout << "CT: " << curr_tail->val << " ";
                // if (curr_tail_next)
                //     cout << "CTN: " << curr_tail_next->val << " ";
                // cout << "CV: " << curr->val << " ";
                // cout << "C: " << count << endl;
                auto ret = reverseLinkedList(curr_head, curr_tail_next);
                if (firstTime) {
                    returnHead = ret.first;
                    firstTime = false;
                } else {
                    // cout << ret.second->val << endl;
                    // if (curr_tail_next)
                    //     cout << curr_tail_next->val << "\n";
                    curr_head_prev->next = ret.first;
                }
                curr_head_prev = curr_head;
                curr_head = curr_tail_next;
                curr = ret.second;
                curr_tail = nullptr;
                curr_tail_next = nullptr;
            }
            count++;
        }
        return returnHead;
    }

    pair<ListNode*, ListNode*> reverseLinkedList(ListNode* head,
                                                 ListNode* tail) {
        /*
            1->2->3->X
            1 = Head
            3 = Tail
            3->2->1->X
            Change 1: New last node next needs to be X
            Change 2: Stop reversing once you hit tail->next node
        */
        pair<ListNode*, ListNode*> kPtrs;
        ListNode *prev = nullptr, *curr = head;
        while (curr != tail) {
            auto temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        kPtrs.first = prev;
        kPtrs.second = head;
        if (tail) {
            kPtrs.second->next = tail;
        }
        return kPtrs;
    }
};