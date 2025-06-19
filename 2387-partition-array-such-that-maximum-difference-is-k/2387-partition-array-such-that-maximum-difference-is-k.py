class Solution(object):
    def partitionArray(self, nums, k):
        nums.sort()
        c=0
        i=0
        while i<len(nums):
            c+=1 
            start=nums[i]
            while i<len(nums)and nums[i]-start<=k:
                i+=1
        return c
        return c