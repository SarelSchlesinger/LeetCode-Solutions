# time complexity: O(n*log(n))
# space complexity: O(n)

class Solution(object):
    def findRelativeRanks(self, score):
        answer = [[val, index] for index, val in enumerate(score)]
        answer.sort(key=lambda pair: pair[0], reverse=True)
        for i in range(len(score)):
            if i > 2:
                answer[i][0] = str(i + 1)
            elif i == 0:
                answer[i][0] = "Gold Medal"
            elif i == 1:
                answer[i][0] = "Silver Medal"
            else:
                answer[i][0] = "Bronze Medal"
        answer.sort(key=lambda pair: pair[1])
        return [pair[0] for pair in answer]