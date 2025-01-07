# time complexity:  O(n)
# space complexity: O(1)

class Solution(object):
    def romanToInt(self, s):
        symbol_to_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s) - 1):
            if symbol_to_value[s[i]] < symbol_to_value[s[i + 1]]:
                res -= symbol_to_value[s[i]]
            else:
                res += symbol_to_value[s[i]]
        return res + symbol_to_value[s[-1]]