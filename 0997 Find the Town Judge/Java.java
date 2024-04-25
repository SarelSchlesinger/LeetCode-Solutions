class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] giveTrust = new int[n + 1];
        int[] receiveTrust = new int[n + 1];
        for (int[] tru: trust) {
            giveTrust[tru[0]] += 1;
            receiveTrust[tru[1]] += 1;
        }
        for (int j = 1; j < giveTrust.length; j++) {
            if (giveTrust[j] == 0 && receiveTrust[j] == n - 1) return j;
        }
        return -1;
    }
}