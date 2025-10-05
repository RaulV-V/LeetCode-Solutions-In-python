# Here is both solutions, the first ran much faster and is much more readable
# The seocnd solution though is the classic two pointer solution included just to show the method



class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 0:
            return True

        only_alnum = "".join(c for c in s if c.isalnum())
        only_alnum = only_alnum.upper()
        rev = only_alnum[::-1]
        if only_alnum == rev: return True
        return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 0:
            return True

        only_alnum = "".join(c for c in s if c.isalnum())
        only_alnum = only_alnum.upper()
        i = 0
        n = len(only_alnum)
        while i < n:
            if only_alnum[n - i - 1] != only_alnum[i]:
                return False
            i += 1
        return True