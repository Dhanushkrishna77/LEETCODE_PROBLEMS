class Solution(object):
    def buildArray(self, nums):
        n=len(nums)
        a=[0]*n
        for i in range(n):
            a[i]=nums[nums[i]]
        return a
