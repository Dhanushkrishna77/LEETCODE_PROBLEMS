class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length;
        int[] res = new int[n];
        int ind=0;
        int i=0;
        while(i<n){
            if(nums[i] < pivot){
                res[ind] = nums[i];
                ind++;
            }
            i++;
      }
      i = 0;
        while(i<n){
            if(nums[i] == pivot){
                res[ind] = nums[i];
                ind++;
            }
            i++;
      }

         i=0;
        while(i<n){
            if(nums[i] > pivot){
                res[ind] = nums[i];
                ind++;
            }
            i++;
      }
      return res;  
    }
}