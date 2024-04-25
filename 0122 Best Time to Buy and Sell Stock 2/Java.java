// time complexity: O(n)
// space complexity: O(1)

class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int i = 1;
        while (i < prices.length) {
            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1];
            }
            i++;
        }
        return profit;
    }
}