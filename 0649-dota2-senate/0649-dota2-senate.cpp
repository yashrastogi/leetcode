class Solution {
public:
    string predictPartyVictory(string senate) {
        unordered_map<char, queue<int>> senators;
        for (int i = 0; i < senate.size(); ++i) {
            senators[senate[i]].push(i);
        }

        int i = 0;
        while (true) {
            if (senators['R'].empty()) {
                return "Dire";
            } else if (senators['D'].empty()) {
                return "Radiant";
            }
            if (senators['R'].front() == i) {
                senators['R'].pop();
                senators['D'].pop();
                senators['R'].push(i);
            } else if (senators['D'].front() == i) {
                senators['D'].pop();
                senators['R'].pop();
                senators['D'].push(i);
            }
            i = (i + 1) % senate.size();
        }
    }
};