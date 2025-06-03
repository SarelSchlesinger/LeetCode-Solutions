// time complexity:  O(n^2)
// space complexity: O(1)

class Solution {
    public boolean check(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int counter = 0;
            for (int j = 0; j < nums.length - 1; j++) {
                if (nums[(i + j) % nums.length] <= nums[(i + j + 1) % nums.length]) counter++;
                else break;
            }
            if (counter + 1 == nums.length) return true;
        }
        return false;
    }
}