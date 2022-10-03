class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> sumVec;
        for(int i=0; i<nums.size(); i++){
            int sum = nums[i];
            for(int j=0; j<i; j++){
                sum += nums[j];
            }
            sumVec.push_back(sum);
            
        }
        return sumVec;
    }
};