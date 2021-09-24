class Solution {
   public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ret, row;
        int chars = 0;
        for (string w : words) {
            int tempWidth = chars + row.size() + w.length();
            if (tempWidth > maxWidth) {
                ret.push_back(convertToString(row, chars, maxWidth));
                row.clear();
                chars = 0;
            }
            row.push_back(w);
            chars += w.length();
        }
        if (row.size()) {
            string temp = "";
            for (string w : row) temp += w + " ";
            temp.pop_back();
            int spaces = maxWidth - temp.size();
            for (int i = 0; i < spaces; i++) temp += " ";
            ret.push_back(temp);
        }
        return ret;
    }

    string convertToString(vector<string> row, int chars, int maxWidth) {
        string ret = "";
        int totalSpaces = maxWidth - chars;
        int idx = 0;
        for (int i = 0; i < totalSpaces; i++)
            row[idx++ % max((unsigned long)1, row.size() - 1)] += " ";
        for (auto w : row) ret += w;
        return ret;
    }
};