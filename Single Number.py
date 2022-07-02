# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
# Input: nums = [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = nums.count(i)

        for i in dic:
            if dic[i] == 1:
                return i


        # xor = 0
        # for i in nums:
        #     xor = xor ^ i
        #     return xor

