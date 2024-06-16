# first approach
class Solution(object):
    def numSteps(self, s):
        steps = 0
        num = 0
        for i in range(len(s)):
            if s[-(1 + i)] == '1':
                num += 2 ** i
        while num > 1:
            steps += 1
            if num % 2 == 1:
                num += 1
            else:
                num /= 2
        return steps
        
# second approach
class Solution(object):
    def numSteps(self, s):
        steps = 0
        while s != '1':
            if s[-1] == '0':
                s = s[:-1]
            else:
                i = s[::-1].find('0')
                if i == -1:
                    s = '1' + '0' * len(s)
                else:
                    s = s[:len(s) - 1 - i] + '1' + '0' * i
            steps += 1
        return steps