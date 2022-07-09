class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
        int flag = 1;
        if(strs.size() == 1){
            return strs[0];
        }
        else{
            for(int i=0; i<strs[0].length() && flag; i++){
                for(int j=0; j<strs.size(); j++){
                    if(strs[j][i]!=strs[0][i]){
                        flag = 0;
                        break;

                    }
                
                }
                res = (flag) ? res+strs[0][i]: res;
            }
            return res;
        }
    }
};