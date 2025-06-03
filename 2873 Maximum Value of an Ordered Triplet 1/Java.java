// first approach - brute force
// time complexity:  O(n^3)
// space complexity: O(1)
class Solution {
    public long maximumTripletValue(int[] nums) {
        long res = 0;
        for (int i = 0 ; i < nums.length - 2 ; i++) {
            for (int j = i + 1 ; j < nums.length - 1 ; j++) {
                for (int k = j + 1 ; k < nums.length ; k++) {
                    res = Math.max(res, (long) (nums[i] - nums[j]) * nums[k]);
                }
            }
        }
        return res;
    }
}

// second approach
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