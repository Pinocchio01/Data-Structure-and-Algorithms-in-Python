# palindromic number

##class Solution:
##    def isPalindrome(self, x: int) -> bool:
##        return str(x) == str(x)[::-1]

# solution 2

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        s = str(x)
        n = len(s)
        L,R = 0, n - 1
        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False
        else:
            return True
