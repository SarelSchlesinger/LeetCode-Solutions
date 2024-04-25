class Solution(object):
    def maxFrequencyElements(self, nums):
        maxFreq = totalFreq = 0
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] == maxFreq:
                totalFreq += maxFreq
            elif freq[num] > maxFreq:
                maxFreq += 1
                totalFreq = maxFreq
        return totalFreq