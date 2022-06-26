# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        z=0

        for i in nums:
            if i != val:
                nums[z] = i
                z += 1
        return z

