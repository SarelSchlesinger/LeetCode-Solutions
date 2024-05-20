# recursive approach
class Solution(object):
    def fib(self, n):
        if n <= 1: return n
        return self.fib(n - 1) + self.fib(n - 2)
        
# dynamic programming approach
class Solution(object):
    def fib(self, n):
        if n <= 1: return n
        F = [0, 1]
        while n > 1:
            F.append(F[-1] + F[-2])
            n -= 1
        return F[-1]