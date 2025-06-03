// time complexity:  O(n)
// space complexity: O(n)

class Solution {
    public String clearDigits(String s) {
        StringBuilder stringBuilder = new StringBuilder();
        for (Character c : s.toCharArray()) {
            if (Character.isLetter(c)) stringBuilder.append(c);
            else stringBuilder.setLength(stringBuilder.length() - 1);
        }
        return stringBuilder.toString();
    }
}