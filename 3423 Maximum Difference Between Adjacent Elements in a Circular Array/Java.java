// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int res = Math.abs(nums[0] - nums[nums.length - 1]);
        for (int i = 0 ; i < nums.length - 1 ; i++) {
            res = Math.max(res, Math.abs(nums[i] - nums[i + 1]));
        }
        return res;
    }
}