class Solution(object):
    def countCompleteSubarrays(self, nums):
        s=[]
        c=0
        k= len(set(nums))
        for r in range(len(nums)):
            s.append(nums[r])
            while len(set(s))==k:
                c+=len(nums)-r
                s.pop(0)
        return c