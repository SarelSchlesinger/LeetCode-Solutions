class Solution(object):
    def fizzBuzz(self, n):
        L = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5 == 0: 
                    L.append("FizzBuzz")
                else:
                    L.append("Fizz")
            elif i % 5 == 0:
                L.append("Buzz")
            else:
                L.append(str(i))
        return L