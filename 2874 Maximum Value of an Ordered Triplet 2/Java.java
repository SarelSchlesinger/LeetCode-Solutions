// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public long maximumTripletValue(int[] nums) {
        long res = 0;
        long a = 0;     // The variable a represents the value of nums[i]
        long b = 0;     // The variable a represents the value of nums[i] - nums[j]
        for (int k = 0 ; k < nums.length ; k++) {
            res = Math.max(res, b * nums[k]);
            b   = Math.max(b, a - nums[k]);
            a   = Math.max(a, nums[k]);
        }
        return res;
    }
}