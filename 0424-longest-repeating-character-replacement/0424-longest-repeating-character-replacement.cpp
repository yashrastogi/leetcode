class Solution {
public:
    int characterReplacement(string s, int k) {
        map<char, int> char_freq;
        int max_len = 0, most_freq = 0;
        for (int j = 0, i = 0; j < s.size(); j++) {
            char_freq[s[j]]++;
            most_freq = max(most_freq, char_freq[s[j]]);
            int curr_window_length = j - i + 1;
            if (curr_window_length - most_freq > k) {
                char_freq[s[i]]--;
                i++;
                curr_window_length = j - i + 1;
            }
            max_len = max(max_len, curr_window_length);
        }

        return max_len;
    }
};
