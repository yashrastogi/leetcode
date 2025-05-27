class Solution {
public:
    vector<string> substrings;
    stack<char> brackets;
    string temp = "";

    vector<string> generateParenthesis(int n) {
        recurse(0, 2 * n);
        return substrings;
    }

    void recurse(int index, int maxLen) {
        if (index == maxLen) {
            if(!brackets.size()) substrings.push_back(temp);
            return;
        }
        if (brackets.size() < maxLen / 2) {
            temp += "(";
            brackets.push('(');
            recurse(index + 1, maxLen);
            brackets.pop();
            temp.pop_back();
        }
        if (brackets.size()) {
            brackets.pop();
            temp += ")";
            recurse(index + 1, maxLen);
            temp.pop_back();
            brackets.push('(');
        }
    }

    bool isBalanced(string brackets) {
        stack<char> br;
        for (char c : brackets) {
            if (c == '(')
                br.push('(');
            else if (br.size())
                br.pop();
            else
                return false;
        }
        if (br.size())
            return false;
        return true;
    }
};
