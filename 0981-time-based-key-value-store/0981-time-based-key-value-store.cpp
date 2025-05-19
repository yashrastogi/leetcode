class TimeMap {
public:
    map<string, deque<pair<int, string>>> data;
    TimeMap() {

    }
    
    void set(string key, string value, int timestamp) {
        this->data[key].push_front({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        deque<pair<int, string>> &target_vec = this->data[key];
        // cout << "[ ";
        for(auto &pair: target_vec) {
            // cout << pair.first << ' ';
            if (pair.first <= timestamp) {
                // cout << "]\n";
                return pair.second;
            }
        }
        cout << "]\n";
        return "";
    }
};