# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
#
# After doing so, return the array.
#
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(1,len(arr)):
            arr[i-1] = max(arr[i:])

        arr[-1] = -1
        return arr