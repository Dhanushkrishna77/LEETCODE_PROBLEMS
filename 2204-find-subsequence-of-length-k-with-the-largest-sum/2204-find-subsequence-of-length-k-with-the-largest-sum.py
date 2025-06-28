class Solution:
    def maxSubsequence(self, nums, k):
        newNums = [[nums[i], i] for i in range(len(nums))]
        heap = []
        
        for i in range(len(nums)):
            heappush(heap, newNums[i])
            if len(heap) > k:
                heappop(heap)
        
        setOfIndex = set()
        for i in range(len(heap)):
            setOfIndex.add(heap[i][1])

        maxSeq = []
        for i in range(len(nums)):
            if i in setOfIndex:
                maxSeq.append(nums[i])
            
        return maxSeq
	