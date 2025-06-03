// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            if (nums[l] % 2 == 0) {
                l++;
            } else if (nums[r] % 2 == 1) {
                r--;
            } else {
                nums[l] += nums[r];
                nums[r] = nums[l] - nums[r];
                nums[l] -= nums[r];
                l++;
                r--;
            }
        }
        return nums;
    }
}