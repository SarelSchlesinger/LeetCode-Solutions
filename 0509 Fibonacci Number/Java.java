class Solution {
    public int fib(int n) {
        return Stream.iterate(new int[]{0, 1}, i -> new int[]{i[1], i[0] + i[1]})
                .limit(n + 1)
                .map(i -> i[0])
                .skip(n)
                .findFirst()
                .orElse(0);
    }
}