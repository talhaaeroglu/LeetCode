class Solution:

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev, curr = 0, 0
   
        for i in range(len(nums)): 
            temp = curr
            curr = max(nums[i] + prev, curr)
            prev = temp
        
        return curr