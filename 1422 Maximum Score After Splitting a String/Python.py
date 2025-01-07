# time complexity:  O(n)
# space complexity: O(1)

class Solution(object):
    def maxScore(self, s):
        maxScore = left0 = 0
        right1 = s.count('1')
        for i in range(len(s) - 1):
            if s[i] == '0':
                left0 += 1
            else:
                right1 -= 1
            maxScore = max(maxScore, left0 + right1)
        return maxScore