# time complexity:  O(n^2)
# space complexity: O(n)

class Solution(object):
    def minOperations(self, boxes):
        answer = [0] * len(boxes)
        not_empty_boxes = [i for i in range(len(boxes)) if boxes[i] == '1']
        for i in range(len(answer)):
            for j in not_empty_boxes:
                answer[i] += abs(i - j)
        return answer
        