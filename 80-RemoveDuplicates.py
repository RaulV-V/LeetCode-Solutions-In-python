class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointerA = 0
        pointerB = 0
        current = nums[0]
        count = 0
        while pointerB  < len(nums):
            if current == nums[pointerB]:
                count += 1
            else:
                count = 1
                current = nums[pointerB]
            if count < 3:
                nums[pointerA] = nums[pointerB]
                pointerA += 1
            pointerB += 1
        return pointerA

             