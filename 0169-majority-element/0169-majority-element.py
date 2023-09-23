class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numMap = {}
        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                numMap[num] = numMap[num] + 1
        return max(numMap, key= numMap.get)