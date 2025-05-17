class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int> s1_freq(26, 0);
        for (char c : s1)
            s1_freq[c - 'a']++;
        vector<int> window_freq(26, 0);

        for (int right = 0, left = 0; right < s2.size(); right++) {
            window_freq[s2[right] - 'a']++;
            if (right - left + 1 > s1.size()) {
                window_freq[s2[left] - 'a']--;
                left++;
            }
            if (window_freq == s1_freq)
                return true;
        }
        
        return false;
    }
};