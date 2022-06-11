# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        l = m + n - 1

        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[l] = nums1[m-1]
                m = m-1
            else:
                nums1[l] = nums2[n-1]
                n = n-1
            l = l-1

        # fill nums1 with leftover nums2
        while n:
            nums1[l] = nums2[n-1]
            n,l = n-1, l-1