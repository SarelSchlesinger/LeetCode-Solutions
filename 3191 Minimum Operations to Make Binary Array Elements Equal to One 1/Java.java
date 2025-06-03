// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public int minOperations(int[] nums) {
        int counter = 0;
        for (int i = 0 ; i < nums.length - 2 ; i++) {
            if (nums[i] == 0) {
                nums[i] = 1;
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
                counter++;
            }
        }
        return nums[nums.length - 1] * nums[nums.length - 2] == 1 ? counter : -1;
    }
}