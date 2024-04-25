# time complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        time = tickets[k]
        for i in range(len(tickets)):
            if i < k:
                if tickets[i] <= tickets[k]:
                    time += tickets[i]
                else:
                    time += tickets[k]
            elif i > k:
                if tickets[i] < tickets[k]:
                    time += tickets[i]
                else:
                    time += tickets[k] - 1
        return time