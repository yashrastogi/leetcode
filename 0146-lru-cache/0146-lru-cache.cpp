class DLLNode {
public:
    int key, val;
    DLLNode *next, *prev;
    DLLNode(int key, int val) {
        this->val = val;
        this->key = key;
        next = prev = nullptr;
    }
};

class LRUCache {
public:
    unordered_map<int, DLLNode*> data;
    int max_capacity;
    DLLNode *head, *tail;

    LRUCache(int capacity) {
        max_capacity = capacity;
        head = new DLLNode(-2, 0);
        head->next = tail;
        tail = new DLLNode(-1, 0);
        tail->prev = head;
    }

    int get(int key) {
        if (!data.count(key))
            return -1;
        // node -> next , node -> prev
        auto node = data[key];
        removeNode(node);
        insertNode(node);
        return node->val;
    }

    void removeNode(DLLNode* node) {
        DLLNode* nodeAfter = node->next;
        DLLNode* nodeBefore = node->prev;
        nodeBefore->next = nodeAfter;
        nodeAfter->prev = nodeBefore;
    }

    void insertNode(DLLNode* node) {
        DLLNode *tailBefore = tail->prev;
        tailBefore->next = node;
        node->prev = tailBefore;
        node->next = tail;
        tail->prev = node;
    }

    void put(int key, int value) {
        if (data.count(key)) {
            auto node = data[key];
            node->val = value;
            removeNode(node);
            insertNode(node);
        } else {
            if (data.size() >= max_capacity) {
                DLLNode* toRemoveNode = head->next;
                removeNode(toRemoveNode);
                data.erase(toRemoveNode->key);
                delete (toRemoveNode);
            }
            auto newNode = new DLLNode(key, value);
            insertNode(newNode);
            data[key] = newNode;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */