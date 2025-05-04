class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        ans = 0
        hmap = {}

        for domino in dominoes:
            d = (min(domino), max(domino))
            if d not in hmap:
                hmap[d] = 1
                continue
            ans = ans + hmap[d]
            hmap[d] = hmap[d] + 1
        
        return ans