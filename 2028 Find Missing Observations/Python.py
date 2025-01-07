# time complexity: O(max(m, n))
# space complexity: O(n)

class Solution(object):
    def missingRolls(self, rolls, mean, n):
        target = mean * (len(rolls) + n) - sum(rolls)
        if target > 6 * n or target < n: return []
        res = [target // n] * n
        for i in range(target % n):
            res[i] += 1
        return res