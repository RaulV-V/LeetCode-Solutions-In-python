# Very simple, just read last sequence of letters | O(1) space and O(count + end spaces) time
# I was going to add a word found boolean but count can serve both purposes saving us a byte of data

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in reversed(range(len(s))):
            if count > 0:
                if s[i] == ' ':
                    break
                else:
                    count += 1
            else:
                if s[i] != ' ':
                    count += 1
        return count