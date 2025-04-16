class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        left = ans = tally = 0
        n, d = len(nums), defaultdict(int)

        for right,num in enumerate(nums):    # <-- 1
            tally += d[num]
            d[num] += 1
            
            while tally >= k:                # <-- 2     
                ans+= n - right
                d[nums[left]] -= 1           # <-- 3
                tally -= d[nums[left]]
                left += 1
            
        return ans                           # <-- 4