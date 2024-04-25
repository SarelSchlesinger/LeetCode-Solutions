// using hashmap
// time complexity: O(n)
// space complexity: O(n)
class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> hashmapS = new HashMap<>();
        HashMap<Character, Character> hashmapT = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (!hashmapS.containsKey(s.charAt(i))) {
                hashmapS.put(s.charAt(i), t.charAt(i));
            } else if (hashmapS.get(s.charAt(i)) != t.charAt(i)) {
                return false;
            }
            if (!hashmapT.containsKey(t.charAt(i))) {
                hashmapT.put(t.charAt(i), s.charAt(i));
            } else if (hashmapT.get(t.charAt(i)) != s.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}