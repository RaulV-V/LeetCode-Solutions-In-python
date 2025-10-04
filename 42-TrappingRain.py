#This was a very elegant problem and solution, this is the approach I came up with by taking an idea from the problem 238

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        water = [0] * n

        cur = 0
        for i in range(n):
            if height[cur] <= height[i]:
                for j in range(cur + 1, i):
                    water[j] = height[cur] - height[j]
                cur = i

        cur = n - 1
        for i in reversed(range(n)):
            if height[cur] <= height[i]:
                for j in range(i + 1, cur):
                    fill = height[cur] - height[j]
                    if fill > water[j]:
                        water[j] = fill
                cur = i

        
        return sum(max(0, w) for w in water)