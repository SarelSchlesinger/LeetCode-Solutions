// time complexity: O(log(n))
// space complexity: O(1)

class Solution {
    public int hammingWeight(int n) {
        int res = 0;
        while (n > 0) {
            if (n % 2 == 1) {
                res += 1;
            }
            n /= 2;
        }
        return res;
    }
}