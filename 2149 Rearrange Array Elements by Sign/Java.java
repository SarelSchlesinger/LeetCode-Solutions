class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] res = new int[nums.length];
        int pos_index = 0;
        int neg_index = 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                res[pos_index] = nums[i];
                pos_index += 2;
            } else {
                res[neg_index] = nums[i];
                neg_index += 2;
            }
        }
        return res;
    }
}