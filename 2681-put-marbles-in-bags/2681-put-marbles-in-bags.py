from typing import List
from itertools import pairwise
from heapq import nlargest, nsmallest

class Solution:
    def putMarbles(self, A: List[int], k: int) -> int:
        B = [a + b for a, b in pairwise(A)]
        return sum(nlargest(k - 1, B)) - sum(nsmallest(k - 1, B))
