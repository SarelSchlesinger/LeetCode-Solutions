class Solution(object):
    def uniqueOccurrences(self, arr):
        d = Counter(arr)
        return True if len(d.values()) == len(set(d.values())) else False