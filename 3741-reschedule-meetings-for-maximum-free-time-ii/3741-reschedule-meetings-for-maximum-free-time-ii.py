class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        gaps = []
        gaps.append(startTime[0])
        n = len(startTime)
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])
        res = max(gaps)

        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)
        prefix[0] = gaps[0]

        for i in range(1, n + 1):
            prefix[i] = max(prefix[i - 1], gaps[i])
        suffix[-1] = gaps[-1]
        for i in range(n - 1, -1, -1):
            suffix[i] = max(suffix[i + 1], gaps[i])
        
        for i in range(n):
            gap = gaps[i] + gaps[i + 1]
            interval = endTime[i] - startTime[i]

            left = prefix[i - 1] if i > 0 else float('-inf')
            right = suffix[i + 2] if i < n - 1 else float('-inf')
            remaining = max(left, right)

            if remaining >= interval:
                gap += interval
            res = max(res, gap)
        return res