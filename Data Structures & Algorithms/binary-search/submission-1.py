class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) - 1
        while start_index <= end_index:
            mid = start_index + ((end_index - start_index) // 2)
            if target < nums[mid]:
                end_index = mid - 1
            elif target == nums[mid]:
                return mid
            else:
                    start_index = mid + 1
        return -1
        

        