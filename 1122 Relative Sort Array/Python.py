# time Complexity: O(m * log(m) + n)
# space complexity: O(m)

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        hm = Counter(arr1)
        k = 0
        for i in arr2:
            while hm[i] > 0:
                arr1[k] = i
                hm[i] -= 1
                k += 1
        for i in sorted(hm.keys()):
            while hm[i] > 0:
                arr1[k] = i
                k += 1
                hm[i] -= 1
        return arr1