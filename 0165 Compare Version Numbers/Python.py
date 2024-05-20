class Solution(object):
    def compareVersion(self, version1, version2):

        def compare(a, b):
            if int(a) > int(b):
                return 1
            elif int(b) > int(a):
                return -1
            return 0

        numbers1 = version1.split('.')
        numbers2 = version2.split('.')

        if len(numbers2) != len(numbers1):
            if len(numbers2) > len(numbers1):
                numbers1.extend(['0'] * (len(numbers2) - len(numbers1)))
            else:
                numbers2.extend(['0'] * (len(numbers1) - len(numbers2)))
        
        i = 0
        while i < len(numbers1):
            comp = compare(numbers1[i], numbers2[i])
            if comp != 0: return comp
            i += 1
        
        return 0