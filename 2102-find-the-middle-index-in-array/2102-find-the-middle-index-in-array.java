class Solution {
    public int findMiddleIndex(int[] nums) {
        int l=nums.length;
        int sum=0;
        int s=0;
        for(int i=0;i<l;i++)
        {
         sum+=nums[i];
        }
        for(int i=0;i<l;s+=nums[i++])
        {
          if(s*2==sum-nums[i])
          {
            return i;
          }
        }
       return -1;
    }
}