class Solution {
public:
    string s;
    unordered_set<string> dict;
    vector<int> memo;
    int minLen, maxLen;

    bool wordBreak(string s, vector<string>& wordDict) {
        this->s = s;
        dict = unordered_set<string>(wordDict.begin(), wordDict.end());
        minLen = INT_MAX;
        maxLen = 0;
        for (auto& word : wordDict) {
            int len = word.length();
            minLen = min(minLen, len);
            maxLen = max(maxLen, len);
        }
        // memo = vector<int>(s.size(), -1);
        // return topDown();
        memo = vector<int>(s.size() + 1, 0);
        return bottomUp();
    }

    bool bottomUp() {
        memo[0] = true;
        for (int i = 0; i < s.size(); i++)
            for (int len = minLen; len <= maxLen; len++)
                // dp[i] check denotes whether it is possible to reach index i
                // in string using any of the words in dict
                // and if suffix starting from i till ++len is also in dict
                // then dp[i + len] is also possible/true
                // by the end it should calculate if reaching end is possible by
                // using words in dict
                if (i + len <= s.size() && dict.count(s.substr(i, len)) &&
                    memo[i])
                    memo[i + len] = true;
        return memo.back();
    }

    bool topDown(int idx = 0) {
        if (idx == s.size())
            return true;
        if (memo[idx] != -1)
            return memo[idx];

        for (int len = minLen; len <= maxLen && idx + len <= s.size(); ++len)
            if (dict.count(s.substr(idx, len)) && topDown(idx + len))
                return memo[idx] = true;

        return memo[idx] = false;
    }
};
