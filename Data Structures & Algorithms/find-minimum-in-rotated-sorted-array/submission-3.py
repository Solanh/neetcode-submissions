class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] < nums[-1] or nums[0] == nums[-1]:
            return nums[0]
        

        left, right = 0, len(nums) -1
       

        while left <= right:
            mid = (left + right) // 2
            # print(left, mid, right)

            if mid > 0 and nums[mid -1] > nums[mid]:
                return nums[mid]
            elif nums[right] < nums[mid]:
                left = mid +1
            elif nums[left] > nums[mid]:
                right = mid -1
            else:
                if left > 0 and nums[left-1] > nums[left]:
                    return nums[left]
                elif nums[right-1] > nums[right]:
                    return nums[right]
        


        

        
        