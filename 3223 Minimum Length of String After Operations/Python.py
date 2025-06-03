# time Complexity:  O(n)
# space complexity: O(1)

class Solution(object):
    def minimumLength(self, s):
        return sum(1 if i % 2 == 1 else 2 for i in Counter(s).values())