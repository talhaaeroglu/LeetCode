class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sum = 0;
        int temp = 0;
        for(int i=0; i<nums.size(); i++){
            sum += nums[i];
        }
        for (int j=0; j<nums.size(); j++){
            if (temp == (sum-nums[j])/2 && (sum-nums[j]) % 2 == 0){
                return j;
            }
            else{
                temp += nums[j];
            }
        }
        return -1;
    }
};