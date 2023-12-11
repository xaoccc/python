class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        return [len([1 for num in nums1 if num in nums2]), len([1 for num in nums2 if num in nums1])]