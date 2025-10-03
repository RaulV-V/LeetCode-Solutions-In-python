class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        copy = nums[:]
        count = len(nums)
        j = 0
        for i in copy:
            nums[(j + k) % (count)] = i
            j += 1