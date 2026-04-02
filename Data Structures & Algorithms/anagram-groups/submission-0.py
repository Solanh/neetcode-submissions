from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i, s in enumerate(strs):
            d = defaultdict(int)
            for char in s:
                d[char] += 1
            new = True
            for k, v in groups.items():
                if d == v[0][0]:
                    groups[k].append([d, s])
                    new = False
            if new:
                groups[i] = [[d, s]]


        a_g = []
        for v in groups.values():
            g = []
            for c in v:
                g.append(c[1])
            a_g.append(g)
                

        return a_g


        
        



            

