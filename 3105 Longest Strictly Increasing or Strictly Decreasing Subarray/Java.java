// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int max_length = 1, current_increasing = 1, current_decreasing = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                max_length = Math.max(max_length, ++current_increasing);
                current_decreasing = 1;
            } else if (nums[i] < nums[i - 1]) {
                max_length = Math.max(max_length, ++current_decreasing);
                current_increasing = 1;
            } else {
                current_decreasing = 1;
                current_increasing = 1;
            }
        }
        return max_length;
    }
}