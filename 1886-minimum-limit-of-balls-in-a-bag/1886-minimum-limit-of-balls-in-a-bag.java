class Solution {
	public static int minimumSize(int[] nums, int maxOperations) {

		int l = 1;
		int r =	(int)Math.pow(10, 9);
		
		while(l<=r) {
			int mid =  l+(r-l)/2;
			
			if(IsPossible(nums, maxOperations, mid)) {
				r =  mid -1;
			}else { 
				l =  mid + 1;
			}
		}
		return l;

	}

	public static boolean IsPossible(int[] nums, int maxOperations, int k) {

		for (int i = 0; i < nums.length; i++) {

			int val = nums[i];

			int temp = val/k;
			
			
			if(val%k!=0) {
				temp++;
			}
			
			temp--;
			
			maxOperations-=temp;
			
			
			if(maxOperations<0) {
				return false;
			}
		}
		return true;
	}
}