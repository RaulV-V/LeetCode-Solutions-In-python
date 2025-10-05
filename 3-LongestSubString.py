# This is worst case O(n^2) time since we have to search through the entire substring but on average it is much less 
# since there are usually duplicated making our substring smaller and there are only 26 unique letters so worst case is actually 
# O(n * (n % 26)) but still smaller on average, space complexity is O(1) since the max amount of letters possible in seen is 26

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        best = 0

        for right, ch in enumerate(s):
            prev = seen.get(ch, -1)
            if prev >= left:
                left = prev + 1
            seen[ch] = right
            best = max(best, right - left + 1)
        return best 