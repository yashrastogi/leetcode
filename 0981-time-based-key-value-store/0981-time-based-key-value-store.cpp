class TimeMap {
public:
    map<string, vector<pair<int, string>>> data;
    TimeMap() {}

    void set(string key, string value, int timestamp) {
        this->data[key].push_back({timestamp, value});
    }

    string get(string key, int timestamp) {
        vector<pair<int, string>>& target_vec = this->data[key];
        int lo = 0, hi = target_vec.size() - 1;
        string ans = "";
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (target_vec[mid].first > timestamp) {
                // if timestamp of mid exceeds given, go left
                hi = mid - 1;
            } else if (timestamp == target_vec[mid].first) {
                // if timestamp match found return value
                return target_vec[mid].second;
            } else {
                // if data timestamp < given timestamp, temporarily store ans
                // check if higher timestamp within range possible by going
                // right
                ans = target_vec[mid].second;
                lo = mid + 1;
            }
        }
        return ans;
    }
};