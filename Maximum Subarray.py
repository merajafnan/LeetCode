# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        cur = 0
        for n in nums:
            if cur < 0:
                cur = 0
            cur = cur + n
            maxsub = max(maxsub, cur)
        return maxsub
