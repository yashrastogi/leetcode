class Solution {
public:
    vector<string> substrings;
    
    vector<string> generateParenthesis(int n) {
        stack<char> brackets;
        recurse(0, 2 * n, "", 0, 0, brackets);
        return substrings;
    }

    void recurse(int index, int maxLen, string temp, int open, int close, stack<char> &brackets) { 
        // ) stack size nil invalid string
        if(index == maxLen) {
            if(open == close && close == maxLen/2)
                if(isBalanced(temp))
                    substrings.push_back(temp);
            return;
        }
        // cout << temp << endl;
        // open/close cant be more than n 
        
        
        if(open + 1 <= maxLen / 2) {
            brackets.push('(');
            recurse(index + 1, maxLen, temp + "(", open + 1, close, brackets);
            brackets.pop();
        }
        if(close + 1 <= maxLen / 2) {
            if(brackets.size()) {
                recurse(index + 1, maxLen, temp + ")", open, close + 1, brackets);
            }
        }
    }

    bool isBalanced(string brackets) {
        stack<char> br;
        for(char c: brackets) {
            if(c == '(') br.push('(');
            else if (br.size()) br.pop();
            else return false;
        }
        if(br.size()) return false;
        return true;
    }

    bool partialBalance(string str) { 
        stack<char> br;
        for(char c: str) {
            if(c == '(') br.push('(');
            else if (br.size()) br.pop();
            else return false;
        }
        return true;
    }

};

