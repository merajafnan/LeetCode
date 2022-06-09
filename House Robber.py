# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0

        # [r1, r2, n, n+1]
        for n in nums:
            temp = max(n+r1, r2)
            r1 = r2
            r2 = temp
        return r2