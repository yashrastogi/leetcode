class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> char_freq(26, 0);
        int max_len = 0, most_freq = 0;
        for (int j = 0, i = 0; j < s.size(); j++) {
            char_freq[s[j] - 'A']++;
            most_freq = max(most_freq, char_freq[s[j] - 'A']);
            if ((j - i + 1) - most_freq > k) {
                char_freq[s[i] - 'A']--;
                i++;
            }
            max_len = max(max_len, j - i + 1);
        }

        return max_len;
    }
};
