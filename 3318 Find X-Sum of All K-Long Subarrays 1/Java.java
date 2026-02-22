class Solution {

    public int xSum(int[] nums, int x) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums)
            freq.put(num, freq.getOrDefault(num, 0) + 1);

        if (x >= freq.size()) return Arrays.stream(nums).sum();
        return freq.entrySet().stream()
                   .sorted(Comparator
                                   .comparing(Map.Entry<Integer, Integer>::getValue).reversed()
                                   .thenComparing(Map.Entry.<Integer, Integer>comparingByKey().reversed()))
                   .limit(x)
                   .mapToInt(e -> e.getKey() * e.getValue())
                   .sum();
    }

    public int[] findXSum(int[] nums, int k, int x) {
        int[] res = new int[nums.length - k + 1];
        for (int i = 0 ; i < res.length ; i++) {
            int[] temp = new int[k];
            for (int j = 0 ; j < temp.length ; j++) {
                temp[j] = nums[j + i];
            }
            res[i] = xSum(temp,x);
        }
        return res;
    }
}