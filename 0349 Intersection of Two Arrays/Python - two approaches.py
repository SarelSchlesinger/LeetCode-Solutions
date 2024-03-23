# first approach -  using sets
class Solution(object):
    def intersection(self, nums1, nums2):
        return set(nums1).intersection(nums2)

# second approach - using two pointers
class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not res or nums1[i] > res[-1]:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res