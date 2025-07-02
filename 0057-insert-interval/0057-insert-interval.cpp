class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& ivs, vector<int>& newi) {
        vector<vector<int>> ans;
        for (int i = 0; i < ivs.size(); i++) {
            auto& intr = ivs[i];
            if (intr[1] < newi[0] || intr[0] > newi[1]) {
                ans.push_back(intr);
            } else {
                newi[0] = min(newi[0], intr[0]);
                newi[1] = max(newi[1], intr[1]);
            }
        }
        auto it = lower_bound(ans.begin(), ans.end(), newi[0],
                              [](const vector<int>& interval, int value) {
                                  return interval[0] < value;
                              });
        ans.insert(it, newi);
        return ans;
    }
};