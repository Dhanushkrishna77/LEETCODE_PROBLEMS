class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1, self.nums2 = nums1, nums2
        self.nums2ToFreqMap = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2ToFreqMap[self.nums2[index]] -= 1
        self.nums2ToFreqMap[self.nums2[index] + val] += 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        ans = 0
        for elem in self.nums1:
            ans += self.nums2ToFreqMap[tot - elem]
        return ans