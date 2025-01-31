class Solution {
    private int[] dr = {-1, 0, 1, 0};
    private int[] dc = {0, 1, 0, -1};
    private int n;
    
    public int largestIsland(int[][] grid) {
        n = grid.length;
        // Use a map to store island ID -> size
        Map<Integer, Integer> islandSizes = new HashMap<>();
        // Start island IDs from 2 to avoid confusion with 1s in the grid
        int islandId = 2;
        int maxSize = 0;
        
        // First pass: label each island with unique ID and calculate sizes
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    int size = dfs(grid, r, c, islandId);
                    islandSizes.put(islandId, size);
                    maxSize = Math.max(maxSize, size);
                    islandId++;
                }
            }
        }
        
        // If there's no 0, return the size of the largest island
        if (maxSize == n * n) return maxSize;
        
        // Second pass: try to flip each 0 to 1 and calculate resulting island size
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) {
                    // Use set to avoid counting same island multiple times
                    Set<Integer> neighborIslands = new HashSet<>();
                    
                    // Check all 4 directions
                    for (int i = 0; i < 4; i++) {
                        int newR = r + dr[i];
                        int newC = c + dc[i];
                        
                        if (isValid(newR, newC) && grid[newR][newC] > 1) {
                            neighborIslands.add(grid[newR][newC]);
                        }
                    }
                    
                    // Calculate total size after connecting all neighboring islands
                    int totalSize = 1; // Start with 1 for the flipped cell
                    for (int id : neighborIslands) {
                        totalSize += islandSizes.get(id);
                    }
                    maxSize = Math.max(maxSize, totalSize);
                }
            }
        }
        
        return maxSize;
    }
    
    private int dfs(int[][] grid, int r, int c, int islandId) {
        if (!isValid(r, c) || grid[r][c] != 1) {
            return 0;
        }
        
        grid[r][c] = islandId;
        int size = 1;
        
        // Visit all 4 directions
        for (int i = 0; i < 4; i++) {
            size += dfs(grid, r + dr[i], c + dc[i], islandId);
        }
        
        return size;
    }
    
    private boolean isValid(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < n;
    }
}