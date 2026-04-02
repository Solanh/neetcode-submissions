class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        trips = []
        # print(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i != 0:
                continue

            left = i +1
            right = len(nums) -1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                    
                elif s > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    # print(i)
                    trips.append([nums[i], nums[left], nums[right]])
                    # print(i, left, right)
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                    left += 1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                    


        return trips
            

            




            

        