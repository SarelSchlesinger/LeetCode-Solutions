# first approach - brute force
# time complexity:  O(n^2)
# space complexity: O(n)
class Solution(object):
    def finalPrices(self, prices):
        answer = prices[:]
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    answer[i] -= prices[j]
                    break
        return answer

# second approach - monotonic stack
# time complexity:  O(n)
# space complexity: O(n)
class Solution(object):
    def finalPrices(self, prices):
        answer = prices[:]
        stack = list()
        for i in range(len(prices) - 1, -1, -1):
            while len(stack) > 0 and stack[-1] > prices[i]:
                stack.pop()
            if len(stack) > 0:
                answer[i] -= stack[-1]
            stack.append(prices[i])
        return answer