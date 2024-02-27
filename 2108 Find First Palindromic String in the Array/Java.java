class Solution {
    public String firstPalindrome(String[] words) {
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words[i].length(); j++) {
                if (words[i].charAt(j) != words[i].charAt(words[i].length() - 1 - j)) { 
                    break;
                }
                if (j == words[i].length() - 1) { 
                    return words[i];
                }
            }
        }
        return "";
    }
}