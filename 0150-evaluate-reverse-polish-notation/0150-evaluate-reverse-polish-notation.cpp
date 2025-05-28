class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> numbers;
        for(int i = 0; i < tokens.size(); i++) {
            if(tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/") {
                int num2 = numbers.top();
                numbers.pop();
                int num1 = numbers.top();
                numbers.pop();
                if(tokens[i] == "+") numbers.push(num1 + num2);
                if(tokens[i] == "-") numbers.push(num1 - num2);
                if(tokens[i] == "/") numbers.push(num1 / num2);
                if(tokens[i] == "*") numbers.push(num1 * num2);
            } else {
                numbers.push(stoi(tokens[i]));
            }
        }
        return numbers.top();
    }
};
