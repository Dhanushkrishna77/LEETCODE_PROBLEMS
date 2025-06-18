class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        ans = []
        size3 = []
        n = len(nums) / 3

        def checkdiff(arr):
            a,b,c = arr
            if b - a <= k and c - a <= k and c - b <= k:
                return True
            return False
        for num in nums:
            size3.append(num)
            if len(size3) == 3 and checkdiff(size3):
                ans.append(size3)
                size3 = []

        if len(ans) == n:
            return ans
        else: 
            return []
                

        