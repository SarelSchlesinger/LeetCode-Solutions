// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        for (char letter: letters) {
            if (letter > target) return letter;
        }
        return letters[0];
    }
}