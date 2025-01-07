// time complexity:  O(n)
// space complexity: O(n)

class Solution {
    public boolean checkIfExist(int[] arr) {
        HashSet<Integer> hs = new HashSet<>();
        for (int num : arr) {
            if (hs.contains(2 * num)) return true;
            if (num % 2 == 0 && hs.contains(num / 2)) return true;
            hs.add(num);
        }
        return false;
    }
}