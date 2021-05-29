class Solution {
  public:
  int coinChange(vector<int>& coins, int amount, int idx = 0) {
    if(amount < 1) return 0;
    vector<int> count(amount, 0);
    return coinChange2(coins, amount, count);
  }

  int coinChange2(vector<int>& coins, int amount, vector<int>& count) {
    if(amount < 0) return -1;
    if(amount == 0) return 0;
    
    if(count[amount - 1] != 0) return count[amount - 1];
    
    int min = INT_MAX;
    for(int coin: coins) {
      int res = coinChange2(coins, amount - coin, count);
      if(res >= 0 && res < min) 
        min = 1 + res;
    }
    return count[amount - 1] = (min == INT_MAX) ? -1 : min;
  }
};