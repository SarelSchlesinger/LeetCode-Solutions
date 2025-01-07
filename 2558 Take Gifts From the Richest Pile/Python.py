# time complexity:  O(n + k * log(n))
# space complexity: O(n)

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-gift for gift in gifts]
        heapq.heapify(maxHeap)
        for _ in range(k):
            heapq.heappush(maxHeap, -floor(sqrt(-maxHeap[0])))
            heapq.heappop(maxHeap)
        return -sum(maxHeap)