// time complexity:  O(n)
// space complexity: O(n)

class Solution {
    public int findLucky(int[] arr) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : arr) freq.put(num, freq.getOrDefault(num, 0) + 1);
        return freq.entrySet().stream()
                   .filter(e -> Objects.equals(e.getKey(), e.getValue()))
                   .map(Map.Entry::getKey)
                   .max(Integer::compareTo)
                   .orElse(-1);
    }
}