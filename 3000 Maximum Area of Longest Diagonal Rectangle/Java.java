// time complexity:  O(n)
// space complexity: O(1)

class Solution {
	public int areaOfMaxDiagonal(int[][] dimensions) {
        double maxDiagonal = 0;
        int maxArea = 0;
        for (int[] rectangle : dimensions) {
            double diagonal = Math.sqrt(rectangle[0] * rectangle[0] + rectangle[1] * rectangle[1]);
            int area = rectangle[0] * rectangle[1];
            if (diagonal == maxDiagonal) {
                maxArea = Math.max(area, maxArea);
            }
            else if (diagonal > maxDiagonal) {
                maxDiagonal = diagonal;
                maxArea = area;
            }
        }
        return maxArea;
    }
}