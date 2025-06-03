// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int counter = 0;
        for (int x : arr) {
            if (x % 2 == 1) {
                counter++;
                if (counter == 3) return true;
            } else {
                counter = 0;
            }
        }
        return false;
    }
}