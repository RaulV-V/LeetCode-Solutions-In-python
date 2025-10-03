class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjumps = nums[0]
        i = 1
        if(len(nums) == 1):
            return True
        while i <= maxjumps:
            if nums[i] + i > maxjumps:
                maxjumps = nums[i] + i
            if maxjumps >= len(nums) - 1:
                return True
            i += 1
        return False    
            