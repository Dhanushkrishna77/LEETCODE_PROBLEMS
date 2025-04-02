class Solution(object):
    def maximumTripletValue(self, nums):
        n = len(nums)
        mv = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i<j<k:
                        v = (nums[i] - nums[j]) * nums[k]
                        if v > mv:
                            mv = v
                            v = 0
        return mv
        