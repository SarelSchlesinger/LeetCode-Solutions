# time complexity:  O(n)
# space complexity: O(1)

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        counter = 0
        for i in arr:
            if i % 2 == 1:
                counter += 1
                if counter == 3:
                    return True
            else:
                counter = 0
        return False