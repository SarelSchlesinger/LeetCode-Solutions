// time complexity:  O(n^2)
// space complexity: O(1)

class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int res = fruits.length;
        for (int fruit : fruits) {
            for (int i = 0 ; i < baskets.length ; i++) {
                if (fruit <= baskets[i]) {
                    baskets[i] = 0;
                    res--;
                    break;
                }
            }
        }
        return res;
    }
}