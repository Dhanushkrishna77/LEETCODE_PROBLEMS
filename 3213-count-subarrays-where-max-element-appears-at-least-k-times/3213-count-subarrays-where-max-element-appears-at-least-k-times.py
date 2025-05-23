class Solution:
    def countSubarrays(self, nums, k):
        arr = []
        max_num = max(nums)
        for i in range(len(nums)):
            if nums[i] == max_num:
                arr.append(i)
        if len(arr) < k:
            return 0
        lip = -1
        count = 0
        for i in range(len(arr) - k + 1):
            li = arr[i]
            ri = arr[i + k - 1]
            subs = (li - lip) * (len(nums) - ri)
            count += subs
            lip = li
        return count