class Solution {
   public:
    int romanToInt(string s) {
        unordered_map<char, int> map{{'I', 1},   {'V', 5},   {'X', 10},
                                     {'L', 50},  {'C', 100}, {'D', 500},
                                     {'M', 1000}};
        int ret = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (i == s.length() - 1)
                ret += map[c];
            else {
                switch (c) {
                    case 'I':
                        if (s[i + 1] == 'V' || s[i + 1] == 'X')
                            ret -= 1;
                        else
                            ret += 1;
                        break;
                    case 'X':
                        if(s[i + 1] == 'L' || s[i + 1] == 'C')
                            ret -= 10;
                        else
                            ret += 10;
                        break;
                    case 'C':
                        if(s[i + 1] == 'D' || s[i + 1] == 'M')
                            ret -= 100;
                        else
                            ret += 100;
                        break;
                    default:
                        ret += map[c];
                }
            }
        }
        return ret;
    }
};