# time complexity: O(n * log(n))
# space complexity: O(n)

class Solution(object):
    def sortPeople(self, names, heights):
        return [tup[0] for tup in sorted(zip(names, heights), key=lambda tup: tup[1], reverse=True)]