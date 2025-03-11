class Solution {
    public int numberOfSubstrings(String s) {
        int i = 0, j = 0, ans = 0, len = s.length(), ct;
        HashMap<Character, Integer> mp = new HashMap<>();
        
        while (j < len) {
            mp.put(s.charAt(j), mp.getOrDefault(s.charAt(j), 0) + 1);
            
            while (mp.size() == 3) {
                ans += (len - j);
                ct = mp.get(s.charAt(i));
                --ct;
                
                if (ct == 0) {
                    mp.remove(s.charAt(i));
                } else {
                    mp.put(s.charAt(i), ct);
                }
                
                ++i;
            }
            ++j;
        }
        return ans;
    }
}