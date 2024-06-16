# time Complexity: O(n * log(n))
# space complexity: O(n)

class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        res = 0
        for i in range(len(seats)):
            res += abs(seats[i] - students[i])
        return res