// using hashmap
// time Complexity: O(n)
// space complexity: O(1)

class Solution {
    public int longestPalindrome(String s) {
        int res = 0;
        boolean flag = false;
        HashMap<Character, Integer> hm = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            hm.put(c, hm.getOrDefault(c, 0) + 1);
        }
        for (int num : hm.values()) {
            if (num % 2 == 0) {
                res += num;
            } else {
                flag = true;
                res += num - 1;
            }
        }
        return flag ? res + 1 : res;
    }
}