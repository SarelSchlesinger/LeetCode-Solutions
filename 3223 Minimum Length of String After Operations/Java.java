// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public int minimumLength(String s) {
        Map<Character, Integer> frequency_map = new HashMap<>();
        for (char c : s.toCharArray()) {
            frequency_map.put(c, frequency_map.getOrDefault(c, 0) + 1);
        }
        int res = 0;
        for (int i : frequency_map.values()) {
            if (i % 2 == 1) res += 1;
            else res += 2;
        }
        return res;
    }
}