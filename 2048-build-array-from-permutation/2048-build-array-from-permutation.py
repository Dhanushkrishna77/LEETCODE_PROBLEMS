class Solution(object):
    def buildArray(self, nums):
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            ans[i] = nums[nums[i]]
        return ans
