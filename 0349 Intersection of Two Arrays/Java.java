class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = Arrays.stream(nums1)
                .boxed()
                .collect(Collectors.toSet());
        return Arrays.stream(nums2)
                .boxed()
                .filter(set1::contains)
                .distinct()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}