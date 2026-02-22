// time complexity:  O(n * log(n))
// space complexity: O(log(n))

class Solution {
    public int minimumDifference(int[] nums, int k) {
        Arrays.sort(nums);
        if (k == nums.length)
            return nums[nums.length - 1] - nums[0];
        int diff = Integer.MAX_VALUE;
        for (int i = 0 ; i <= nums.length - k ; i++) {
            diff = Math.min(diff, nums[i + k - 1] - nums[i]);
        }
        return diff;
    }
}