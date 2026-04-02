class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for s in strs:
            e += s
            e += "thisisabreak"

        return e

    def decode(self, s: str) -> List[str]:
        # print(s)
        s = s.strip()
        l = s.split("thisisabreak")
        # print(l)
        return l[0:len(l)-1]
