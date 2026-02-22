class Solution {

    public boolean noZero(int x) {
        while (x > 0) {
            if ((x % 10) == 0) return false;
            x /= 10;
        }
        return true;
    }

    public int[] getNoZeroIntegers(int n) {
        int a = 1, b = n - 1;
        while (true) {
            if (noZero(a) && noZero(b)) {
                return new int[]{a, b};
            }
            a++;
            b--;
        }
    }
}