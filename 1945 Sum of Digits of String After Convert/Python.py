# time complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def getLucky(self, s, k):
        
        s = ''.join([str(ord(letter) - 96) for letter in s])
        
        for _ in range(k):
            counter = 0
            for digit in s:
                counter += int(digiSt)
            s = str(counter)
        return int(s)