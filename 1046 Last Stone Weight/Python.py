class Solution(object):
    def lastStoneWeight(self, stones):
        maxHeap = list()
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        while len(maxHeap) > 1:
            heaviest = -maxHeap[0]
            heapq.heappop(maxHeap)
            almost_heaviest = -maxHeap[0]        
            heapq.heappop(maxHeap)
            if heaviest > almost_heaviest:
                heapq.heappush(maxHeap, almost_heaviest - heaviest)
        return 0 if len(maxHeap) == 0 else -maxHeap[0]