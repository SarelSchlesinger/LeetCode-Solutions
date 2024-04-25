// first approach - using set
// time complexity: O(n)
// space complexity: O(n)

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> setNums = new HashSet<Integer>();
        for (int num: nums) {
			// time complexity of add() method: O(1)
            if(!setNums.add(num)) {
                return true;
            }
        }
        return false;
    }
}

// second approach - using sorting
// time complexity: O(n*log(n))
// space complexity: O(1)

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int i = 1;
        while (i < nums.length) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
            i++;
        }
        return false;
    }
}