// time complexity:  O(n)
// space complexity: O(n)

class Solution {

    private int[] nums;

    public Solution(int[] nums) {
        this.nums = nums.clone();
    }
    
    public int[] reset() {
        return this.nums;
    }
    
    // Fisher-Yates shuffle
	public int[] shuffle() {
        Random r = new Random();
        int[] arr = this.nums.clone();
        for (int i = arr.length - 1 ; i > 0 ; i--) {
            int j = r.nextInt(i + 1);
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        return arr;
    }

}