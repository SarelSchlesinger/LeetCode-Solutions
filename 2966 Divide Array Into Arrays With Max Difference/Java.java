class Solution {
    public int[][] divideArray(int[] nums, int k) {
       Arrays.sort(nums);
	   int[][] dividedArr = new int[nums.length / 3][3];
	   for(int i = 0 ; i < nums.length ; i++) {
		   dividedArr[i / 3][i % 3] = nums[i];
		   if (i % 3 == 2) {
			   if (nums[i] - nums[i - 2] > k) return new int[0][0];
			}
        } 
        return dividedArr;
    }
}