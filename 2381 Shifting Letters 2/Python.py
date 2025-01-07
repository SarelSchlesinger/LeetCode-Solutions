# time complexity:  O(m + n)
# space complexity: O(n)

class Solution(object):
    def shiftingLetters(self, sN, shiftsM):
        shift_diff = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            if direction == 1:
                shift_diff[start] += 1
                shift_diff[end + 1] -= 1
            else:
                shift_diff[start] -= 1
                shift_diff[end + 1] += 1
        res = list()
        cumulative_shift = 0
        for i in range(len(s)):
            cumulative_shift += shift_diff[i]
            res.append(chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a')))
        return ''.join(res)