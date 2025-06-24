class Solution:
    def findKDistantIndices(self, nums, key, k):
        key_indices = [i for i, val in enumerate(nums) if val == key]
        result = []
        idx = 0

        for i in range(len(nums)):
            while idx < len(key_indices) and key_indices[idx] + k < i:
                idx += 1
            if idx < len(key_indices) and abs(key_indices[idx] - i) <= k:
                result.append(i)
        return result