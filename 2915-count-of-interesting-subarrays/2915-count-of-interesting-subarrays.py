class Solution:
    def countInterestingSubarrays(self, a: List[int], m: int, k: int) -> int:
        res, p = 0, Counter({0:1})
        for q in accumulate(map(lambda v:v%m==k, a)):
            res += p[(q-k)%m]
            p[q%m] += 1

        return res