// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        Map<String, Integer> pairs = new HashMap<>();
        for (int[] domino : dominoes) {
            String key = Arrays.toString(domino[0] <= domino[1] ? domino : new int[]{ domino[1], domino[0] });
            pairs.put(key, pairs.getOrDefault(key, 0) + 1);
        }
        return pairs.values().stream().mapToInt(i -> i * (i - 1) / 2).sum();
    }
}