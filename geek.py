from typing import List

class Solution:
    def solve(self, N : int, a : int , x : List[int]) -> int:
        # code here
        max = 0
        temp = 0
        y = [abs(item-a) for item in x]
        y.sort()
        last = y[len(y)-1]
        last_last = y[len(y)-2]
        max = last + last_last
        return max


        # for i in range (0,N):
        #     for j in range(i+1,N):
        #         temp = abs(a-x[i]) + abs(a-x[j])
        #         if (temp > max):
        #             max = temp
        # return max