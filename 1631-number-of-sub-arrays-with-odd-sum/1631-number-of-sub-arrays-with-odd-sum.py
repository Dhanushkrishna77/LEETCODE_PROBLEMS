class Solution(object):
    def numOfSubarrays(self, arr):
        c = cum = odds_c = 0
        evens_c= 1
        for num in arr:
            cum+=num
            if cum%2:
              c+= evens_c
              odds_c+=1
            else:
              c+= odds_c
              evens_c+=1
        return c%(7+10**9)