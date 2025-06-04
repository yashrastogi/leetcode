
class TrieNode {
public:
    TrieNode* children[26];
    bool isEnd = false;
    TrieNode() { fill_n(children, 26, nullptr); }
};

class WordDictionary {
public:
    TrieNode* root;
    WordDictionary() { root = new TrieNode(); }

    void addWord(string w) {
        TrieNode* curr = root;
        for (int i = 0; i < w.size(); i++) {
            if (!curr->children[w[i] - 'a'])
                curr->children[w[i] - 'a'] = new TrieNode();
            curr = curr->children[w[i] - 'a'];
        }
        curr->isEnd = true;
    }

    bool search(string w) { return searchR(w, 0, root); }

    bool searchR(const string& w, int j = 0, TrieNode* curr = nullptr) {
        if (j == w.size())
            return curr->isEnd;
        if (w[j] == '.') {
            for (int i = 0; i < 26; i++)
                if (curr->children[i] && searchR(w, j + 1, curr->children[i]))
                    return true;
            return false;
        }
        if (!curr->children[w[j] - 'a'])
            return false;
        return searchR(w, j + 1, curr->children[w[j] - 'a']);
    }
};