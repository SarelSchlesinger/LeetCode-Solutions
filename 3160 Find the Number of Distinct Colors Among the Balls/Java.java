// time complexity:  O(n)
// space complexity: O(n)

class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        int[] res = new int[queries.length];
        Map<Integer, Integer> ball_color = new HashMap<>();
        Map<Integer, Integer> color_ball = new HashMap<>();
        for (int i = 0; i < queries.length; i++) {
            int ball = queries[i][0];
            int color = queries[i][1];
            if (ball_color.containsKey(ball)) {
                int prev_color = ball_color.get(ball);
                color_ball.put(prev_color, color_ball.get(prev_color) - 1);
                if (color_ball.get(prev_color) == 0) {
                    color_ball.remove(prev_color);
                }
            }
            color_ball.put(color, color_ball.getOrDefault(color, 0) + 1);
            ball_color.put(ball, color);
            res[i] = color_ball.size();
        }
        return res;
    }
}