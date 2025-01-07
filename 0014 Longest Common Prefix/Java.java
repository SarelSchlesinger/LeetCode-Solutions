class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1) return strs[0];
        Arrays.sort(strs);
        String left = strs[0];
        String right = strs[strs.length - 1];
        return IntStream.range(0, Math.min(left.length(), right.length()))
                .takeWhile(i -> left.charAt(i) == right.charAt(i))
                .mapToObj(i -> String.valueOf(left.charAt(i)))
                .collect(Collectors.joining());
    }
}