class TrieNode {
public:
    string word = "";
    array<TrieNode*, 26> children = {};
    TrieNode* parent;
    char val;

    TrieNode(char val) : val(val) { parent = nullptr; }

    ~TrieNode() {
        for (auto child : children)
            if (child)
                delete child;
    }

    bool isEmptyNode() const {
        if (!word.empty())
            return false;
        for (int i = 0; i < 26; ++i)
            if (children[i])
                return false;
        return true;
    }

    void prune() {
        if (!parent)
            return;
        auto curr = this;
        while (curr && curr->isEmptyNode()) {
            auto p = curr->parent;
            if (p)
                p->children[curr->val - 'a'] = nullptr;
            curr = p;
        }
    }
};

class Solution {
public:
    TrieNode* root;
    vector<string> res;

    vector<string> findWords(vector<vector<char>>& board,
                             vector<string>& words) {
        res.clear();
        root = new TrieNode('-');
        for (auto& w : words) {
            auto curr = root;
            for (char ch : w) {
                if (!curr->children[ch - 'a']) {
                    curr->children[ch - 'a'] = new TrieNode(ch);
                    curr->children[ch - 'a']->parent = curr;
                }
                curr = curr->children[ch - 'a'];
            }
            curr->word = w;
        }
        for (int r = 0; r < (int)board.size(); r++)
            for (int c = 0; c < (int)board[0].size(); c++)
                if (root->children[board[r][c] - 'a'])
                    dfs(board, root->children[board[r][c] - 'a'], r, c);
        delete root;
        return res;
    }

    void dfs(vector<vector<char>>& board, TrieNode* node, int r, int c) {
        if (!node || board[r][c] == '#')
            return;

        if (node->word.size()) {
            res.push_back(node->word);
            node->word = "";
            node->prune();
        }

        if (node->isEmptyNode())
            return;

        char ch = board[r][c];
        board[r][c] = '#';

        static const vector<vector<int>> directions(
            {{0, 1}, {1, 0}, {-1, 0}, {0, -1}});
        for (auto& d : directions) {
            int newR = r + d[0], newC = c + d[1];
            if (!(newR < 0 || newC < 0 || newR >= board.size() ||
                  newC >= board[0].size())) {
                char nextChar = board[newR][newC];
                if (nextChar != '#' && node->children[nextChar - 'a'])
                    dfs(board, node->children[nextChar - 'a'], newR, newC);
            }
        }

        board[r][c] = ch;
    }
};
