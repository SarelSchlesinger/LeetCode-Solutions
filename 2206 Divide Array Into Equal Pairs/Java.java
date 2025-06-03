// first approach - sorting
// time complexity:  O(n*log(n))
// space complexity: O(log(n))
class Solution {
    public boolean divideArray(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0 ; i < nums.length ; i += 2) {
            if (nums[i] != nums[i + 1]) return false;
        }
        return true;
    }
}

// second approach - map
// time complexity:  O(n)
// space complexity: O(n)
class Solution {
    public boolean divideArray(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        return freq.values().stream().allMatch(i -> i % 2 == 0);
    }
}