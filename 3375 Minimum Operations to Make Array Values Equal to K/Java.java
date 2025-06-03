// time complexity:  O(n)
// space complexity: O(n)

class Solution {
    public int minOperations(int[] nums, int k) {
        Set<Integer> appeared_in_nums = new HashSet<>();
        for (int num : nums) {
            if (num < k) return -1;
            if (num > k) appeared_in_nums.add(num);
        }
        return appeared_in_nums.size();
    }
}