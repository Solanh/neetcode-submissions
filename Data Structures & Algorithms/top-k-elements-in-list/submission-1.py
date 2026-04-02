from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        f = []
        freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        # print(freq)
        for i in range(k):
            f.append(freq[i][0])
        return f
        