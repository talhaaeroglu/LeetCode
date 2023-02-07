class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            if(i==0):
                ret.append(nums[0])
            else:
                last = ret.pop()
                ret.append(last)
                ret.append(last+nums[i])

        return ret