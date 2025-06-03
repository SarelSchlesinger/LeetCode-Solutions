# time complexity:  O(n)
# space complexity: O(n)

class Solution(object):
    def pivotArray(self, nums, pivot):
        head, tail = [], []
        pivot_counter = 0
        for num in nums:
            if num < pivot:
                head.append(num)
            elif num > pivot:
                tail.append(num)
            else:
                pivot_counter += 1
        return head + [pivot] * pivot_counter + tail