// two pointers approach
// time complexity: O(n)
// space complexity: O(1)

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0, j = 0;
        while (i < nums.size()) {
            if (nums[i] != 0) {
                nums[j] = nums[i];
                j++;
            }
            i++;
        }
        for (int k = j; k < nums.size(); k++) {
            nums[k] = 0;
        }     
    }
};