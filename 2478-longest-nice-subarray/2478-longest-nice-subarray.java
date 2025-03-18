class Solution {
    public int longestNiceSubarray(int[] nums) {
        var length = 0;
        for (var start = 0; start < nums.length; start ++)
            for (
                int end = start, mask = 0; 
                end < nums.length && (mask & nums[end]) == 0;
                mask ^= nums[end], length = Math.max(length, ++end - start)
            );
        return length;
    }
}