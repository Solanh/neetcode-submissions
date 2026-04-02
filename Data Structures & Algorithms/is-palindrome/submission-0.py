class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        valid = True

        s = s.lower()
        while valid and l < r:
            
            if s[l].isalnum() and s[r].isalnum() and s[l] == s[r]:
                l += 1
                r -= 1
            elif not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r -= 1
            else:
                valid = False


        return valid

        