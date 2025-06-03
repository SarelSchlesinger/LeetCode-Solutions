// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public boolean canConstruct(String s, int k) {
        if (k > s.length()) return false;
        if (k == s.length()) return true;
        Map<Character, Integer> char_count = new HashMap<>();
        for (char c: s.toCharArray()) {
            char_count.put(c, char_count.getOrDefault(c, 0) + 1);
        }
        return char_count.values().stream().mapToInt(i -> i % 2).sum() <= k;
    }
}