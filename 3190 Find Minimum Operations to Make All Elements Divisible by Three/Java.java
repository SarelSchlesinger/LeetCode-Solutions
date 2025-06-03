// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public int minimumOperations(int[] nums) {
        int res = 0;
        for (int num : nums) {
            if (num % 3 != 0) res++;
        }
        return res;
    }
}