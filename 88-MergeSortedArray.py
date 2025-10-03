# This solution is O(1) space complexity and O(m + n) time complexity

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if (m == 0):
            nums1[:] = nums2 # rewrite the contents of nums1 for basecase
        if (n != 0):
            i = m - 1
            j = n - 1
            k = m + n -1
             
            pointerA = nums1[i]
            pointerB = nums2[j]

            while(i >= 0 and j >= 0):
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
                k -= 1
            while(j >= 0):
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            while(i >= 0):
                nums1[k] = nums1[i]
                i -= 1
                k -= 1