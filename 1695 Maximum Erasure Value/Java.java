// time complexity:  O(n)
// space complexity: O(n)

class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int max_score = 0, score = 0, fast = 0, slow = 0;
        Set<Integer> set = new HashSet<>();
        while (fast < nums.length) {
            if (!set.contains(nums[fast])) {
                set.add(nums[fast]);
                score += nums[fast];
            }
            else {
                max_score = Math.max(max_score, score);
                while (nums[slow] != nums[fast]) {
                    set.remove(nums[slow]);
                    score -= nums[slow];
                    slow++;
                }
                slow++;
            }
            fast++;
        }
        return Math.max(max_score, score);
    }
}