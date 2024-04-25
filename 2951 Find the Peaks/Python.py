# using list comprehension
def findPeaks(self, mountain):
    return [i for i in range(1, len(mountain) - 1) if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]]

# using filter method
class Solution(object):
    def findPeaks(self, mountain):
        return filter(lambda i: mountain[i] > mountain[i + 1] and mountain[i] > mountain[i - 1], range(1, len(mountain) - 1))
        