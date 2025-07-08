class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [event[0] for event in events]
        @lru_cache(None)
        def dp(i: int, remaining: int):
            if i == len(events) or remaining == 0:
                return 0
            res = dp(i + 1, remaining)
            next_index = bisect_right(starts, events[i][1])
            take = events[i][2] + dp(next_index, remaining - 1)
            return max(res, take)

        return dp(0, k)