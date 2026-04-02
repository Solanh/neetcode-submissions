class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <=1:
            return len(s)
        p1,p2 = 0, 0
        best = 0

        sub = set()
        sub.add(s[p1])
        
        while p2 < len(s)-1:
            p2 += 1
            # print(p1, p2, sub)
            if s[p2] in sub:
                # print(1)
                while s[p2] in sub:
                    sub.remove(s[p1])
                    p1 += 1
                    
           
               
            sub.add(s[p2])
            # print(s[p1:p2+1])
            best = max(best, len(s[p1:p2+1]))
        return best


            