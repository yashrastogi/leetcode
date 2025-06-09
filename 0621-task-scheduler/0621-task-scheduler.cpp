template <typename T> using max_heap = priority_queue<T, vector<T>, less<T>>;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> freq;
        for (auto t : tasks)
            freq[t]++;
        // freq task  index
        max_heap<tuple<int, char, int>> sch;
        int cycles = 0;
        for (auto [c, f] : freq)
            sch.push({f, c, -n});

        vector<tuple<int, char, int>> temp;
        int i = 0;
        while (sch.size()) {
            // top element on cooldown
            while (sch.size() && (i - get<2>(sch.top()) <= n)) {
                // top element still on cooldown
                temp.push_back(sch.top());
                sch.pop();
            }
            if (sch.size()) {
                auto top = sch.top();
                sch.pop();
                get<0>(top)--;
                get<2>(top) = i;
                if (get<0>(top) > 0) {
                    sch.push(top);
                }
                cycles++;
            } else {
                // idle
                cycles++;
            }
            i++;
            while (temp.size()) {
                sch.push(temp.back());
                temp.pop_back();
            }
        }

        // input by highest freq elements
        // for most suitable candidate, check when last occured and compare
        // against cooldown n

        return cycles - 1;
    }
};