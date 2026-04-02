class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        for i in range(n+1):
            counts.append(i.bit_count())

        return counts