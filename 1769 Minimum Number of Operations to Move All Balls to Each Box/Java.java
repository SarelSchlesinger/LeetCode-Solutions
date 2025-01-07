// time complexity:  O(n^2)
// space complexity: O(n)

class Solution {
    public int[] minOperations(String boxes) {
        int[] answer = new int[boxes.length()];
        List<Integer> not_empty_boxes = new ArrayList<>();
        for (int i = 0; i < boxes.length(); i++) {
            if (boxes.charAt(i) == '1') {
                not_empty_boxes.add(i);
            }
        }
        for (int i = 0; i < answer.length; i++) {
            for (int j : not_empty_boxes) {
                answer[i] += Math.abs(i - j);
            }
        }
        return answer;
    }
}