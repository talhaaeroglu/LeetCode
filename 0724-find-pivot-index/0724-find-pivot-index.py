class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        ind = 0
        sum = 0
        for num in nums:
            sum += num
        for i in range(len(nums)):
            if (sum-nums[i])%2 == 0 and temp == (sum-nums[i])/2 :
                return i
            temp += nums[i]
        return -1