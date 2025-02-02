class Solution {
    public boolean check(int[] nums) {
        int count = 0, iter = 0;
        int len = nums.length;
        if(len == 1)
        {
            return true;
        }
        for(int i = 0; ; i++)
        {
            if(nums[i%len] > nums[(i+1)%len])
            {
                count++;
            }
            iter++;
            if(count == 2 && iter <= len)
            {
                return false;
            }
            if(iter > len)
            {
                return true;
            }
        }
    }
}