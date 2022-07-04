# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums