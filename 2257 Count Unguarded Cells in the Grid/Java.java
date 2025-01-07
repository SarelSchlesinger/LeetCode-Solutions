// time complexity:  O(m * n + guards.length * (m + n))
// space complexity: O(m * n)

class Solution {
    
    public static int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        
        // time complexity: O(m * n)
        // space complexity: O(m * n)
        int[][] board = new int[m][n];
        
        // time complexity: O(m * n)
        for (int[] guard : guards) {
            board[guard[0]][guard[1]] = 1;
        }
        for (int[] wall : walls) {
            board[wall[0]][wall[1]] = -1;
        }
        
        // time complexity: O(guards.length * (m + n))
        for (int[] guard : guards) {
            // east
            int k = guard[1] + 1;
            while (k < n && board[guard[0]][k] != 1 && board[guard[0]][k] != -1) {
                board[guard[0]][k] = 2;
                k++;
            }
            // west
            k = guard[1] - 1;
            while (k >= 0 && board[guard[0]][k] != 1 && board[guard[0]][k] != -1) {
                board[guard[0]][k] = 2;
                k--;
            }
            // south
            k = guard[0] + 1;
            while (k < m && board[k][guard[1]] != 1 && board[k][guard[1]] != -1) {
                board[k][guard[1]] = 2;
                k++;
            }
            // north
            k = guard[0] - 1;
            while (k >= 0 && board[k][guard[1]] != 1 && board[k][guard[1]] != -1) {
                board[k][guard[1]] = 2;
                k--;
            }
        }
        // time complexity: O(m * n)
        return Math.toIntExact(
                Arrays.stream(board)
                        .flatMapToInt(Arrays::stream)
                        .filter(i -> i == 0)
                        .count()
        );
    }
}