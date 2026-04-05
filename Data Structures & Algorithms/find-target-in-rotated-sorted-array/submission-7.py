class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[left] == target:
                    return left
            elif nums[right] == target:
                return right
            elif target == nums[mid]:
                return mid
            elif nums[mid] < nums[right]:
                if target > nums[mid]:
                    if target > nums[right]:
                        right = mid
                    else:
                        left = mid + 1
                else:
                    right = mid
            elif nums[mid] > nums[right]:
                if target < nums[mid]:
                    if target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                else:
                    return -1