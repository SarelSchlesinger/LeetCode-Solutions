# first approach - using two pointers
class Solution(object):
    def getCommon(self, nums1, nums2):
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]: return nums1[i]
            elif nums1[i] > nums2[j]: j += 1
            else : i += 1
        return -1

# second approach - using sets
class Solution(object):
    def getCommon(self, nums1, nums2):
        nums3 = set(nums1).intersection(nums2)
        return -1 if not nums3 else min(nums3)