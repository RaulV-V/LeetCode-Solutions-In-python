# O(n) time and O(1) space, 0ms run time
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointerA = 1
        pointerB = 1
        while pointerB < len(nums):
            if nums[pointerB] != nums[pointerB -1]:
                nums[pointerA] = nums[pointerB]
                pointerA += 1
            pointerB += 1
        return pointerA