class Solution {
  public:
    Node *copyRandomList(Node *head) {
        Node *copyNodeHead = new Node(-INT_MAX);
        unordered_map<Node *, Node *> copyNodesMap;
        // Create copies of original nodes and set next on copies
        auto copyNodeCurr = copyNodeHead;
        for (auto originalNode = head; originalNode; originalNode = originalNode->next) {
            copyNodeCurr = copyNodeCurr->next = new Node(originalNode->val);
            copyNodesMap.emplace(originalNode, copyNodeCurr);
        }
        // Use the mapping of original to copy nodes to set random pointers
        copyNodeCurr = copyNodeHead->next;
        for (auto originalNode = head; originalNode; originalNode = originalNode->next) {
            copyNodesMap[originalNode]->random =
                copyNodesMap[originalNode->random];
            copyNodeCurr = copyNodeCurr->next;
        }
        return copyNodeHead->next;
    }
};