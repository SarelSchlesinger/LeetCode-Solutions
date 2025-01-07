// time complexity:  O(n + k * log(n))
// space complexity: O(n)
class Solution {
    public long pickGifts(int[] gifts, int k) {
        PriorityQueue<Long> maxHeap = new PriorityQueue<>(Arrays.stream(gifts).mapToLong(i -> -i).boxed().toList());
        while (k > 0) {
            maxHeap.add(-(long) Math.sqrt(-maxHeap.poll()));
            k--;
        }
        return -maxHeap.stream().reduce(0L, Long::sum);
    }
}