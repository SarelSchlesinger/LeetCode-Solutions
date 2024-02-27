// Dynamic Programming
class Solution {
    public long largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        long[] sumArray = new long[nums.length];
        sumArray[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            sumArray[i] = sumArray[i - 1] + nums[i];
        }
        for (int i = nums.length - 1; i >= 2; i--) {
            if (nums[i] < sumArray[i - 1]) {
                return sumArray[i];
            }
        }
        return -1;
    }
}