// time complexity:  O(n^2)
// space complexity: O(n^2)

class Solution {
    public int tupleSameProduct(int[] nums) {
        Map<Integer, Integer> hm = new HashMap<>();
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                hm.put(nums[i] * nums[j], hm.getOrDefault(nums[i] * nums[j], 0) + 1);
            }
        }
        return hm.values().stream()
                .filter(i -> i > 1)
                .mapToInt(i -> 4 * i * (i - 1))
                .sum();
    }
}