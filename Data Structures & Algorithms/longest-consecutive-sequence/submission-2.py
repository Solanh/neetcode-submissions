class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        nums.sort()
        best = 0
        current = 1
        for i in range(len(nums)-1):
            # print(i)
            # print(nums[i], nums[i+1])
            if nums[i] +1 == nums[i+1]:
                current += 1
                
            else:
                current = 1
            best = max(best, current)
        return best 
                

