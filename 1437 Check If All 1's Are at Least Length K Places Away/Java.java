// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int currentZeros = 0;
        boolean one = false;
        for (int num : nums) {
            if (num == 0) currentZeros++;
            else {
                if (one == false) one = true;
                else if (currentZeros < k) return false;
                currentZeros = 0;
            }
        }
        return true;
    }
}