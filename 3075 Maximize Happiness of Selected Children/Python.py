# first approach - greedy algorithm by sorting
# time complexity: O(n*log(n))
# space complexity: O(n)

class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)    # Timsort
        i = res = 0
        while k > 0:
            res += max(happiness[i] - i, 0)
            k -= 1
            i += 1
        return res
        
# second approach - greedy algorithm by heap
# time complexity: O(log(n)*(n + k))
# space complexity: O(n)

class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        maxHeap = list()
        for i in happiness:
            heapq.heappush(maxHeap, -i)
        res = 0
        for i in range(k):
            res += max(-heapq.heappop(maxHeap) - i, 0)
        return res