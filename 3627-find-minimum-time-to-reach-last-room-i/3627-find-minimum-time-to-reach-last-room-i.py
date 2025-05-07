import heapq
from typing import List

class Solution:
    
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        n, m = len(moveTime), len(moveTime[0])
        
        pq = [(0, 0, 0)]  # (time, row, col)
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        while pq:
            time, row, col = heapq.heappop(pq)
            
            if row == n - 1 and col == m - 1:
                return time
            
            for i in range(4):
                nrow, ncol = row + drow[i], col + dcol[i]
                
                if 0 <= nrow < n and 0 <= ncol < m:
                    max_time = max(time + 1, moveTime[nrow][ncol] + 1)
                    if dist[nrow][ncol] > max_time:
                        dist[nrow][ncol] = max_time
                        heapq.heappush(pq, (max_time, nrow, ncol))
        
        return -1