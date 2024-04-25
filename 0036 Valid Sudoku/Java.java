// time complexity: O(n^2)

class Solution {
	
    public boolean isValidSudoku(char[][] board) {
        int boxSize = (int) Math.sqrt(board.length);
        for (int i = 0; i < board.length; i++) {
				// row
            if (isNotValid(board[i])) {
                return false;
            }
            char[] col = new char[board.length];
            char[] box = new char[board.length];
            for (int j = 0; j < board.length; j++) {
                col[j] = board[j][i];
                box[j] = board[(i / boxSize) * boxSize + j / boxSize][(i % boxSize) * boxSize + j % boxSize];
            }
				// column
            if (isNotValid(col) ||
				// box
				isNotValid(box)) {
                return false;
            }
        }
        return true;
    }

    public static boolean isNotValid(char[] arr) {
        Set<Character> hs = new HashSet<>();
        for (char ch : arr) {
            if (hs.contains(ch)) {
                return true;
            }
            if (ch != '.') {
                hs.add(ch);
            }
        }
        return false;
    }
	
}