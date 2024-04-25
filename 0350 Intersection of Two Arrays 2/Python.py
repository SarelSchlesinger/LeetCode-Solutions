# first approach - using two pointers
# time complexity: O(m*log(m) + n*log(n))
# space complexity: O(m + n)

class Solution(object):
    def intersect(self, nums1, nums2):
        res = list()
        nums1.sort()    # using Timsort
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
        

# second approach - using hashmap
# time complexity: O(m + n)
# space complexity: O(min(m, n))

class Solution(object):
    def intersect(self, nums1, nums2):
        res = list()
        counter = Counter(nums1 if len(nums1) < len(nums2) else nums2)
        for num in (nums1 if len(nums1) >= len(nums2) else nums2):
            if counter[num] > 0:
                res.append(num)
                counter[num] -= 1
        return res