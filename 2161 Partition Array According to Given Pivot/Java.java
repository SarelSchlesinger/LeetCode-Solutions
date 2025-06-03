// time complexity:  O(n)
// space complexity: O(n)

class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        List<Integer> less = new ArrayList<>();
        List<Integer> greater = new ArrayList<>();
        int pivot_counter = 0;
        for (int num : nums) {
            if (num < pivot) less.add(num);
            else if (num > pivot) greater.add(num);
            else pivot_counter++;
        }
        for (int i = 0 ; i < less.size() ; i++) {
            nums[i] = less.get(i);
        }
        for (int i = 0 ; i < pivot_counter ; i++) {
            nums[less.size() + i] = pivot;
        }
        for (int i = 0 ; i < greater.size() ; i++) {
            nums[less.size() + pivot_counter + i] = greater.get(i);
        }
        return nums;
    }
}