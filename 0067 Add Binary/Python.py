# first approach
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

# second approach
class Solution(object):
    def addBinary(self, a, b):
        if len(a) > len(b):
            b = b.zfill(len(a))
        else:
            a = a.zfill(len(b))
        res = str()
        carry = '0'
        for i in reversed(range(len(a))):
            if a[i] == '0' and b[i] == '0':
                if carry == '0':
                    res = '0' + res
                else:
                    res = '1' + res
                    carry = '0'
            elif a[i] == '0' or b[i] == '0':
                if carry == '0':
                    res = '1' + res
                else:
                    res = '0' + res
                    carry = '1'
            else:
                if carry == '0':
                    res = '0' + res
                    carry = '1'
                else:
                    res = '1' + res
                    carry = '1'
        if carry == '1':
            res = '1' + res
        return res