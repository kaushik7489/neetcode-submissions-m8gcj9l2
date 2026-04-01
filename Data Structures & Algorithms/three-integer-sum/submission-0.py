class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                if (0 - nums[i] - nums[j]) in seen:
                    temp = sorted([(0 - nums[i] - nums[j]), nums[i], nums[j]])
                    if temp not in result:
                        result.append(temp)
                        seen.add(nums[j])
                    else:
                        seen.add(nums[j])
                else:
                    seen.add(nums[j])
        return result