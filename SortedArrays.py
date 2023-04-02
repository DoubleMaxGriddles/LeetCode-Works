class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            max_left_1 = float('-inf') if partition1 == 0 else nums1[partition1-1]
            min_right_1 = float('inf') if partition1 == m else nums1[partition1]
            max_left_2 = float('-inf') if partition2 == 0 else nums2[partition2-1]
            min_right_2 = float('inf') if partition2 == n else nums2[partition2]
            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if (m + n) % 2 == 0:
                    return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2.0
                else:
                    return float(max(max_left_1, max_left_2))
            elif max_left_1 > min_right_2:
                right = partition1 - 1
            else:
                left = partition1 + 1
