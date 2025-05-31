/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if (!root)
            return {};
        auto q = queue<TreeNode*>({root});
        vector<int> res2;
        while (q.size()) {
            int levelSize = q.size();
            int currVal = -1;
            for (int i = 0; i < levelSize; i++) {
                auto curr = q.front();
                q.pop();
                currVal = curr->val;
                if (curr->left)
                    q.push(curr->left);
                if (curr->right)
                    q.push(curr->right);
            }
            res2.push_back(currVal);
        }
        return res2;
    }
};
