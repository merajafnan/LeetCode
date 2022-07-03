# Contains Duplicate
# Input: nums = [1,2,3,1]
# Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        return (True if len(nums) != len(set(nums)) else False)