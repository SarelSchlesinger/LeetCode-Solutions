// time complexity:  O(n * log(n))
// space complexity: O(log(n))

class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int absDiff = Integer.MAX_VALUE;
        List<List<Integer>> res = new ArrayList<>();;
        for (int i = 0 ; i < arr.length - 1 ; i++) {
            int curAbsDiff = arr[i + 1] - arr[i];
            if (curAbsDiff < absDiff) {
                absDiff = curAbsDiff;
                res.clear();
                res.add(List.of(arr[i], arr[i + 1]));
            }
            else if (curAbsDiff == absDiff)
                res.add(List.of(arr[i], arr[i + 1]));
        }
        return res;
    }
}