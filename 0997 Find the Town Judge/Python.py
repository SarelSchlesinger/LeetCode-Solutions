class Solution(object):
    def findJudge(self, n, trust):
        giveTrust = [0] * (n + 1)
        receiveTrust = [0] * (n + 1)
        for give, receive in trust:
            giveTrust[give] += 1
            receiveTrust[receive] += 1
        for i in range(1, n + 1):
            if giveTrust[i] == 0 and receiveTrust[i] == n - 1:
                return i
        return -1