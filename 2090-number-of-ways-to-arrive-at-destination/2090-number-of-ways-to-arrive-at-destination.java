import java.util.*;

class Solution {
    public int countPaths(int n, int[][] roads) {
        final int MOD = 1_000_000_007;
        
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        
        for (int[] road : roads) {
            int u = road[0], v = road[1], time = road[2];
            graph.get(u).add(new int[]{v, time});
            graph.get(v).add(new int[]{u, time});
        }
        
        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[]{0, 0}); 
        
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[0] = 0;
        
        int[] ways = new int[n];
        ways[0] = 1;
        
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long time = cur[0];
            int node = (int) cur[1];

            if (time > dist[node]) continue; 
            
            for (int[] neighbor : graph.get(node)) {
                int nextNode = neighbor[0];
                long newTime = time + neighbor[1];

                if (newTime < dist[nextNode]) {
                    dist[nextNode] = newTime;
                    pq.offer(new long[]{newTime, nextNode});
                    ways[nextNode] = ways[node]; 
                } else if (newTime == dist[nextNode]) {
                    ways[nextNode] = (ways[nextNode] + ways[node]) % MOD; 
                }
            }
        }
        
        return ways[n - 1];
    }
}