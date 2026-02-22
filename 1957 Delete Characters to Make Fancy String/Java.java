// time complexity:  O(n)
// space complexity: O(n)

class Solution {
    public String makeFancyString(String s) {
                return IntStream.range(0, s.length())
                        .filter(i -> i < 2 || s.charAt(i) != s.charAt(i - 1) || s.charAt(i) != s.charAt(i - 2))
                        .mapToObj(i -> String.valueOf(s.charAt(i)))
                        .collect(Collectors.joining());
    }
}