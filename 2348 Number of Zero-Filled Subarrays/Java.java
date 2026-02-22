// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long res = 0, current = 0;
        for (int num : nums) {
            if (num == 0) {
                res += ++current;
            } else {
                current = 0;
            }
        }
        return res;
    }
}