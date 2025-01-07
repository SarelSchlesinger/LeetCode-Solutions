// time complexity: O(m * n)

class Solution {
    public int strStr(String haystack, String needle) {
    return IntStream.range(0, haystack.length() - needle.length() + 1)
                .filter(i -> needle.equals(haystack.subSequence(i, i + needle.length())))
                .findFirst()
                .orElse(-1);
    }
}