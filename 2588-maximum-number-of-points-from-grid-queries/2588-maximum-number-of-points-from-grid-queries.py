class Solution:
    def maxPoints(self, grid, queries):
        rows, cols = len(grid), len(grid[0])
        q_len = len(queries)
        queries_idx = sorted((val, i) for i, val in enumerate(queries))
        
        min_heap = [(grid[0][0], 0, 0)] 
        visited = set()
        visited.add((0, 0))
        result = [0] * q_len
        count = 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for query, i in queries_idx:
            while min_heap and min_heap[0][0] < query:
                value, r, c = heappop(min_heap)
                count += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))
            result[i] = count
        
        return result