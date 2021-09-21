class Solution {
 public:
  int myAtoi(string s) {
    int i = 0;
    long long retNum = 0;
    bool positive = true;
    while (s[i] == ' ' && i++ < s.length())
      ;
    if (s[i] == '-') {
      positive = false;
      i++;
    } else if (s[i] == '+') {
      i++;
    }
    for (; i < s.length(); i++) {
      int num = charToInt(s[i]);
      if (num != -1) {
        retNum = (retNum * 10) + num;
        if (retNum > INT_MAX && !positive)
          retNum = (long long)INT_MAX + 1;
        else if (retNum > INT_MAX)
          retNum = INT_MAX;
      } else {
        break;
      }
    }
    return positive ? (int)retNum : (int)-retNum;
  }

  int charToInt(char c) {
    if (c >= '0' && c <= '9')
      return c - '0';
    return -1;
  }
};