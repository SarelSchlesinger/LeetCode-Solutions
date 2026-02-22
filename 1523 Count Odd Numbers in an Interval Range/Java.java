// time complexity:  O(1)
// space complexity: O(1)

class Solution {
    public int countOdds(int low, int high) {
        if (high % 2 == 1) high++;
        if (low % 2 == 1) low--;
        return (high - low) / 2;
    }
}