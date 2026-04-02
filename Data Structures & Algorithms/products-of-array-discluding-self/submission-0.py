class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a1, a2 = [], []
        if len(nums) == 0:
            return nums
        elif len(nums) == 1:
            return [0]

        for i in range(len(nums)):
            if i == 0:
                a1.append(nums[i])
            else:
                a1.append(a1[i-1] * nums[i])
        
        for i, num in enumerate(reversed(nums)):
            # print(i)
            if i == 0:
                a2.append(num)
            else:
                a2.append(a2[i-1] * num)
            
            # print(a2, nums[i])
        

        final = []
        a2.reverse()
        print(a1)
        print(a2)

        for i in range(len(nums)):
            if i == 0:
                final.append(a2[i+1])
            elif i == len(nums)-1:
                final.append(a1[-2])
            else:
                final.append(a1[i-1] * a2[i+1])
        return final


        