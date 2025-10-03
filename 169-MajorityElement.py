#linear time and constant space using the Boyer Moore method
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        majority = 0
        for val in nums:
            if count == 0:
                majority = val
            if val == majority:
                count += 1
            else:
                count -= 1
        return majority