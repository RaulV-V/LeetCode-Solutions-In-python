class Solution:
    def jump(self, nums: List[int]) -> int:

        if(len(nums) <= 1):
            return 0

        maxjump = 0
        current = 0
        jumps = 0

        for i in range(len(nums) - 1):  
            maxjump = max(maxjump, i + nums[i])
            if i == current:        
                jumps += 1
                current = maxjump
                if current >= len(nums) - 1:
                    break
        return jumps