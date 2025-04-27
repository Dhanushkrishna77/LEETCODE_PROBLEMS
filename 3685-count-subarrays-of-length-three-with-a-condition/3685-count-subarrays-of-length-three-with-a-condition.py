class Solution(object):
    def countSubarrays(self, nums):
        c=0
        for i in range(2, len(nums)):
            if 2*(nums[i]+nums[i-2])==nums[i-1]:
                c+=1
        return c