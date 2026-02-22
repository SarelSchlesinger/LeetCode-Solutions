// bottom-up
// time complexity:  O(n)
// space complexity: O(n)
class Solution {
    public int climbStairs(int n) {
        if (n < 3) return n;
        int[] tabulation = new int[n];
        tabulation[0] = 1;
        tabulation[1] = 2;
        for (int i = 2 ; i < n ; i++) {
            tabulation[i] = tabulation[i - 1] + tabulation[i - 2];
        }
        return tabulation[n - 1];
    }
}

// top-down
// time complexity:  O(n)
// space complexity: O(n)
class Solution {
    public static int climbStairs(int n) {
        int[] memoization = new int[n];
        return climbStairsHelper(n, memoization);
    }

    public static int climbStairsHelper(int n, int[] memoization) {
        if (n < 3) return n;
        if (memoization[n - 1] != 0) return memoization[n - 1];
        memoization[n - 1] = climbStairsHelper(n - 1, memoization) + climbStairsHelper(n - 2, memoization);
        return memoization[n - 1];
    }
}