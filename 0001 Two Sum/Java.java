// first approach - brute force
// time complexity: O(n^2)
// space complexity: O(1)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }
}


// second approach - using hashmap
// time complexity: O(n)
// space complexity: O(n)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> hash_map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (hash_map.containsKey(target - nums[i])) {
                return new int[]{hash_map.get(target - nums[i]), i};
            } else {
                hash_map.put(nums[i], i);
            }
        }
        return null;
    }
}