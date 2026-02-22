// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public String largestGoodInteger(String num) {
       String res = "";
        for (int i = 1 ; i < num.length() - 1 ; i++) {
            String substring = num.substring(i - 1, i + 2);
            if (substring.charAt(0) == substring.charAt(1) && substring.charAt(1) == substring.charAt(2)) {
                if (res.isEmpty() || substring.compareTo(res) > 0) res = substring;
            }
        }
        return res;
    }
}