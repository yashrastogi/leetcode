class Solution {
public:
    int maxVowels(string s, int k) {
        unordered_set<char> vowels_list = {'a', 'e', 'i', 'o', 'u'};
        int vowels_count = 0;

        for (int i = 0; i < k; ++i) {
            if (vowels_list.find(s[i]) != vowels_list.end()) 
                vowels_count++;
        }

        int max_vowels_count = vowels_count;
        int start_prev = 0;

        for (int end = k; end < s.length(); ++end) {
            if (vowels_list.find(s[end]) != vowels_list.end()) 
                vowels_count++;
            if (vowels_list.find(s[start_prev]) != vowels_list.end()) 
                vowels_count--;
            start_prev++;
            max_vowels_count = max(max_vowels_count, vowels_count);
        }
        return max_vowels_count;
    }
};