# Solution includes print statements to show expected output and debug but not included in final submission

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        best = inf

        for right in range(len(nums)):
            print("Starting right:", right, "and Left:", left)
            
            curr += nums[right]
            print("Curr:", curr)
            while curr >= target:
                print("Shift right:", right, "and Left:", left)
                
                if (right - left) < best:
                    best = (right - left)
                print("Best: ", best)
                curr -= nums[left]
                left += 1
            print(best)
        if best == inf:
            return 0
        return best + 1

