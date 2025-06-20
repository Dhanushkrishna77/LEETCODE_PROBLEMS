class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        nN, nS, nW, nE, output = 0, 0, 0, 0, 0
        for i, c in enumerate(s):
            if c == 'N': nN += 1
            if c == 'S': nS += 1
            if c == 'W': nW += 1
            if c == 'E': nE += 1
            output = max(output, abs(nN - nS) + abs(nE - nW) + 2*(min(k, min(nN, nS) + min(nE, nW))))
        return output