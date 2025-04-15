from sortedcontainers import SortedList

class BIT:
    def __init__(self, size):
        self.bit = [0] * (size + 1)

    def getSum(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & (-idx)
        return s

    def addValue(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] += val
            idx += idx & (-idx)

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        idx = {}
        for i, x in enumerate(nums2):
            idx[x] = i
        
        for i in range(n):
            nums1[i] = idx[nums1[i]]

        ans = 0
        seen = SortedList()
        bit = BIT(n)
        for x in nums1:
            cnt = seen.bisect_right(x)
            ans += bit.getSum(x+1)
            bit.addValue(x+1, cnt)
            seen.add(x)
        return ans