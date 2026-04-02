from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0

        freq = defaultdict(int)
        max_freq = 0
        
        p1, p2 = 0, 0
     

        while p2 < len(s):
            freq[s[p2]] += 1
            max_freq = max(max_freq, freq[s[p2]])

            while (p2-p1 +1) - max_freq > k:
                freq[s[p1]] -= 1
                p1 += 1
            best = max(best, p2 - p1 +1)

            p2 += 1
        return best



                
                
                



                


        