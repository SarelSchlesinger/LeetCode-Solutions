# first approach - brute force
# time complexity:  O(n * k)
# space complexity: O(1)
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for _ in range(k):
            min_num_index = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[min_num_index]:
                    min_num_index = i
            nums[min_num_index] *= multiplier
        return nums

# second approach - minimum heap
# time complexity:  O(n + k * log(n))
# space complexity: O(n)
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        min_heap = [(value, index) for index, value in enumerate(nums)]
        heapify(min_heap)
        for _ in range(k):
            _, index = heappop(min_heap)
            nums[index] *= multiplier
            heappush(min_heap, (nums[index], index))
        return nums



    