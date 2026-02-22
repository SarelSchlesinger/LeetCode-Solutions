// time complexity:  O(n)
// space complexity: O(n)

class Solution {
    public int[] sumZero(int n) {
        int[] arr = new int[n];
        while (n >= 2) {
            arr[n - 1] = -(n--);
            arr[n - 1] = 1 + n--;
        }
        return arr;
    }
}