class Solution {
public:
    string minWindow(string s, string t) {
        string res = "";
        vector<int> t_freq(58, 0);
        for (char c : t)
            t_freq[c - 'A']++;
        vector<int> s_freq(58, 0);
        bool valid = false;

        for (int right = 0, left = 0; right < s.size(); right++) {
            s_freq[s[right] - 'A']++;
            if (!valid) {
                for (int k = 0; k < 58; k++)
                    if (s_freq[k] < t_freq[k]) {
                        valid = false;
                        break;
                    } else {
                        valid = true;
                    }
            }
            while (left <= right &&
                   (t_freq[s[left] - 'A'] == 0 ||
                    s_freq[s[left] - 'A'] > t_freq[s[left] - 'A'])) {
                s_freq[s[left] - 'A']--;
                left++;
            }
            if ((right - left + 1 < res.size() || res.size() == 0) && valid) {
                res = s.substr(left, right - left + 1);
            }
        }

        return res;
    }
};
