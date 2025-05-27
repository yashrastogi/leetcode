class Solution {
public:
    vector<string> substrings;

    vector<string> generateParenthesis(int n) {
        recurse(0, 2 * n, "", 0, 0);
        return substrings;
    }

    void recurse(int index, int maxLen, string temp, int open, int close) {
        if (index == maxLen) {
            if (open == close && close == maxLen / 2)
                if (isBalanced(temp))
                    substrings.push_back(temp);
            return;
        }

        if (open + 1 <= maxLen / 2) {
            recurse(index + 1, maxLen, temp + "(", open + 1, close);
        }
        if (close < open) {
            recurse(index + 1, maxLen, temp + ")", open, close + 1);
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

    bool partialBalance(string str) {
        stack<char> br;
        for (char c : str) {
            if (c == '(')
                br.push('(');
            else if (br.size())
                br.pop();
            else
                return false;
        }
        return true;
    }
};
