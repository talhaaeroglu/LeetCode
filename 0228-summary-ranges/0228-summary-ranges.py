class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return []
        prev1 = nums[0]
        prev2 = nums[0]
        index = 1
        res = []
    
        while index < len(nums):
            if prev2 + 1 == nums[index]:
                prev2 = nums[index]
            else:
                if prev1 == prev2:
                    res.append(str(prev1))
                else:
                    res.append(f"{prev1}->{prev2}")
                prev1 = nums[index]
                prev2 = nums[index]
                
            index += 1

        if prev1 == prev2:
            res.append(str(prev1))
        else:
            res.append(f"{prev1}->{prev2}")
            
        return res
            