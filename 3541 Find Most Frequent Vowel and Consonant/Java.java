// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public int maxFreqSum(String s) {
        Map<Character, Integer> vowels = new HashMap<>();
        Map<Character, Integer> consonant = new HashMap<>();
        for (Character c : s.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') vowels.put(c, vowels.getOrDefault(c, 0) + 1);
            else consonant.put(c, consonant.getOrDefault(c, 0) + 1);
        }
        return vowels.values().stream().max(Comparator.comparing(Integer::intValue)).orElse(0) +
               consonant.values().stream().max(Comparator.comparing(Integer::intValue)).orElse(0);
    }
}