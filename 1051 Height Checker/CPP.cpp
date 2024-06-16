// time Complexity: O(n * log(n))
// space complexity: O(n)

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int* expected = new int[heights.size()];
        copy(heights.begin(), heights.end(), expected);
        sort(expected, expected + heights.size());
        int res = 0;
        for (int i = 0; i < heights.size(); i++) {
            if (heights[i] != expected[i]) {
                res++;
            }
        }
        return res;
    }
};