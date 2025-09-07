#include <iostream>

using namespace std;

class Solution {
public:
    unordered_map<string, queue<string>> adj;
    vector<string> it;
    vector<vector<string>> tickets;

    vector<string> findItinerary(vector<vector<string>>& tickets) {
        this->tickets = tickets;
        sort(tickets.begin(), tickets.end());
        for (auto& t : tickets)
            adj[t[0]].emplace(t[1]);
        departFrom("JFK");
        reverse(it.begin(), it.end());
        return it;
    }

    bool departFrom(string s) {
        while (adj[s].size()) {
            string d = adj[s].front();
            adj[s].pop();
            departFrom(d);
        }
        it.emplace_back(s);
        return false;
    }
};
