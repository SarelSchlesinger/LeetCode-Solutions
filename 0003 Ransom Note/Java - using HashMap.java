class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> hashmap = new HashMap<>();
        char currentChar;
        for (int i = 0; i < magazine.length(); i++) {
            currentChar = magazine.charAt(i);
            if (!hashmap.containsKey(currentChar)) {
                hashmap.put(currentChar, 1);
            } else {
                hashmap.put(currentChar, hashmap.get(currentChar) + 1);
            }
        }

        for (int i = 0; i < ransomNote.length(); i++) {
            currentChar = ransomNote.charAt(i);
            if (!hashmap.containsKey(currentChar)) {
                return false;
            } else {
                if (hashmap.get(currentChar) == 0) {
                    return false;
                } else {
                    hashmap.put(currentChar, hashmap.get(currentChar) - 1);
                }
            }
        }
        return true;        
    }
}