class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        sol = []
        for i, value in enumerate(nums):
            comp = target - value
            if comp in seen:
                return [seen[comp], i]
            else:
                seen[value] = i
        return sol
        