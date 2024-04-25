// first approach - using set
// time complexity: O(n)
// space complexity: O(n)

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> setNums;
        for (int num: nums) {
			// time complexity of insert() method: O(1)
            if (!setNums.insert(num).second) {
                return true;
            }
        }
        return false;
    }
};


// second approach - using sorting
// time complexity: O(n*log(n))
// space complexity: O(log(n))

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
		// space complexity of sort() method: O(log(n))
        sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        return false;
    }
};