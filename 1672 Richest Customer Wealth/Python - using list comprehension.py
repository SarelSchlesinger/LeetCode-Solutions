class Solution(object):
    def maximumWealth(self, accounts):
        return max([sum(L) for L in accounts])