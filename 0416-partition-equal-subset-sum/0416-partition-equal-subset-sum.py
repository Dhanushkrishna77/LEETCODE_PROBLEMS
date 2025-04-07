class Solution(object):
    def canPartition(self, nums):
        return not sum(nums)%2 and reduce(lambda a,b:a|(a<<b),nums,1)&(1<<(sum(nums)//2)) > 0