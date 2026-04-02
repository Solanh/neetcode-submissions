class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) -1

        while left < right:
            mid = (left + right) //2

            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        nums1 = nums[0:pivot]
        nums2 = nums[pivot:]

        left, right = 0, len(nums1) -1

        while left <= right:
            mid = (left + right) // 2

            if nums1[mid] == target:
                # print("loa")
                return mid
            elif nums1[mid] > target:
                right = mid -1
            else:
                left = mid + 1

        left, right = 0, len(nums2) -1

        while left <= right:
            mid = (left + right) // 2

            if nums2[mid] == target:
                # print("ello")
                return mid + len(nums1)
            elif nums2[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1

