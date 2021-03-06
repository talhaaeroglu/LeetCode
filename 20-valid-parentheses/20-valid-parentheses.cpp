class Solution {
public:
    bool isValid(string s) {
        stack<int> stack;
        for(int i=0; i<s.length(); i++){
            if(s[i] == '(' || s[i] == '[' || s[i] == '{' ){
                stack.push(s[i]);
            }
            else if((s[i] == '}' || s[i] == ']' || s[i] == ')') && !stack.empty()){
                
                switch(s[i]){
                    case ')':
                        if(stack.top() == '(')
                            stack.pop();
                        else
                            return false;
                        break;
                    case '}':
                        if(stack.top() == '{')
                            stack.pop();
                        else
                            return false;
                        break;
                    case ']':
                        if(stack.top() == '[')
                            stack.pop();
                        else
                            return false;
                        break;
                }
                
            }
            else{
                return false;
            }
                
        }
        if(stack.empty())
            return true;

        else
            return false;
    }
};