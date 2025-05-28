class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            int temp = -1;
            if(!st.empty()) temp = st.top();
            while (!st.empty() && temperatures[temp] < temperatures[i]) {
                res[st.top()] = i - st.top();
                st.pop();
                if(!st.empty()) temp = st.top();
            }
            st.push(i);
        }
        return res;
    }
};