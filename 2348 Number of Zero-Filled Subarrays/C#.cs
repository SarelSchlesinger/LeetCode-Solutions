// time complexity:  O(n)
// space complexity: O(1)

public class Solution {
    public long ZeroFilledSubarray(int[] nums) {
        long res = 0, current = 0;
        foreach (int num in nums) {
            if (num == 0) {
                res += ++current;
            } else {
                current = 0;
            }
        }
        return res;
    }
}