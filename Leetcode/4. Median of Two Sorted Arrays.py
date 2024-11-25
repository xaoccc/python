class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = nums1 + nums2
        merged_arr = sorted(merged_arr)
        middle_idx = len(merged_arr) // 2
        if len(merged_arr) % 2 != 0:
            return merged_arr[middle_idx]
        else:
            return ((merged_arr[middle_idx - 1] + merged_arr[middle_idx])) / 2