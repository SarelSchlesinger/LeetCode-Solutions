# time Complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def firstUniqChar(self, s):
        frequency = [0] * 26
        index = [-1] * 26
        for i, j in enumerate(s):
            frequency[ord(j) - 97] += 1
            index[ord(j) - 97] = i
        res = [pairs[1] for pairs in zip(frequency, index) if pairs[0] == 1]
        return -1 if not res else min(res)