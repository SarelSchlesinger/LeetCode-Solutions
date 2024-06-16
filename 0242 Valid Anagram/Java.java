// using hashmap
// time Complexity: O(n)
// space complexity: O(n)

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        HashMap<Character, Integer> hmS = new HashMap<>();
        HashMap<Character, Integer> hmT = new HashMap<>();
        for (int i = 0; i < t.length(); i++) {
            hmS.put(s.charAt(i), hmS.getOrDefault(s.charAt(i), 0) + 1);
            hmT.put(t.charAt(i), hmT.getOrDefault(t.charAt(i), 0) + 1);
        }
        return hmS.equals(hmT);
    }
}