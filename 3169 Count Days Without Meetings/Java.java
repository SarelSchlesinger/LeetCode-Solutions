// time complexity:  O(n * log(n))
// space complexity: O(n)

class Solution {
    public int countDays(int days, int[][] meetings) {
        Arrays.sort(meetings, Comparator.comparingInt(meeting -> meeting[0]));
        Stack<int[]> meetings_stack = new Stack<>();
        for (int i = 0 ; i < meetings.length ; i++) {
            if (meetings_stack.empty() || meetings[i][0] > meetings_stack.peek()[1]) {
                meetings_stack.push(meetings[i]);
            }
            else if (meetings[i][1] > meetings_stack.peek()[1]) {
                meetings_stack.push(new int[] { meetings_stack.pop()[0], meetings[i][1] });
            }
        }
        return days - meetings_stack.stream().mapToInt(meeting -> meeting[1] - meeting[0] + 1).sum();
    }
}