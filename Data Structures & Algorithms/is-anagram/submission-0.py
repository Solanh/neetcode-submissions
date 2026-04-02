from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d1 = defaultdict(int)
        for l in s:
            d1[l] +=1
        for l in t:
            d1[l] -= 1
        valid = True
        for val in d1.values():
           if val != 0:
            valid = False
        return valid

        

        
        