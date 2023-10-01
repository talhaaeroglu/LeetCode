class Solution:
    memo = []
    def rob(self, nums: List[int]) -> int:
        self.memo = [-1] * len(nums)
        return self.helper(nums, len(nums)-1)

    def helper(self, nums: List[int], index: int) -> int:
        if index < 0:
            return 0
        if self.memo[index] >= 0:
            return self.memo[index]
        result = max(nums[index] + self.helper(nums, index - 2), self.helper(nums, index-1))
        self.memo[index] = result
        return result