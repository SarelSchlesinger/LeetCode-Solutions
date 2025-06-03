// time complexity:  O(1)
// space complexity: O(1)

class Solution {
    public int smallestEvenMultiple(int n) {
        if (n % 2 == 0) return n;
        return 2 * n;
    }
}