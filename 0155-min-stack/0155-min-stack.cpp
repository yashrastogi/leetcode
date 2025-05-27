class MinStack {
public:
    stack<pair<int, int>> data;
    MinStack() {}
    
    void push(int val) {
        int min_val = INT_MAX;
        if(data.size())
            min_val = data.top().second;
        if(val < min_val) 
            data.push({val, val});
        else 
            data.push({val, min_val});
    }
    
    void pop() {
        data.pop();
    }
    
    int top() {
        return data.top().first;
    }
    
    int getMin() {
        return data.top().second;
    }
};