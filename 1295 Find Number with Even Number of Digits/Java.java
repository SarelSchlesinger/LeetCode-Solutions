class Solution {
    public int findNumbers(int[] nums) {
        return Arrays.stream(nums)
                     .mapToObj(Integer::toString)
                     .filter(i -> i.length() % 2 == 0)
                     .mapToInt(i -> 1)
                     .sum();
    }
}