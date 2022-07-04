# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    from collections import Counter
    def majorityElement(self, nums: List[int]) -> int:

        d = {}
        d = Counter(nums)
        for i in d:
            if d[i] > (len(nums)//2):
                return i