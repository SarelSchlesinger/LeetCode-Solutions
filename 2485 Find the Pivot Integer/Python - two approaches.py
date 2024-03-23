# iterative approach
# time complexity: O(n)
class Solution(object):
    def pivotInteger(self, n):
        head = 0
        tail = sum(range(n + 1))
        i = 1
        while head < tail:
            head += i
            tail -= i
            if head == i + tail:
                return i
            i += 1
        return -1
        
# straight forward approach - use of a mathematical formula
# time complexity: O(1)
class Solution(object):
    def pivotInteger(self, n):
        sum = n * (n + 1) // 2
        pivot = int(pow(sum, 0.5))
        return pivot if pivot * pivot == sum else -1