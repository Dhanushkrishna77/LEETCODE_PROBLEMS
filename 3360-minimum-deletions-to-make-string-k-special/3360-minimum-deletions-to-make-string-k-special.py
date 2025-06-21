from collections import Counter


class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        cnt = Counter(word)
        min_del = float('inf')
        for c, mn in cnt.items():
            count = 0
            for ch, num in cnt.items():
                if num < mn:
                    count += num
                if num > mn + k:
                    count += num - (mn + k)
            min_del = min(min_del, count)
        return min_del if min_del != float('inf') else 0