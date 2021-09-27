class Solution {
 public:
  int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
    unordered_set<string> set;
    for (auto x : wordList)
      set.insert(x);
    queue<pair<string, int>> q;
    q.push({beginWord, 1});
    while (q.size() > 0) {
      auto [curr, depth] = q.front();
      q.pop();
      if (curr == endWord)
        return depth;
      for (int pos = 0; pos < curr.size(); pos++) {
        char c = curr[pos];
        for (int a = 0; a < 26; a++) {
          if ('a' + a != c) {
            string temp = curr;
            temp[pos] = 'a' + a;
            if (set.find(temp) != set.end()) {
              set.erase(temp);
              q.push({temp, depth + 1});
              cout << temp << "\n";
            }
          }
        }
      }
    }
    return 0;
  }
};