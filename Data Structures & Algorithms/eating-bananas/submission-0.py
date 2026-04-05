import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        temp = 1
        while left <= right:
            mid = left + ((right - left) // 2)
            hours = 0
            for i in piles:
                hours += math.ceil(i / mid)
            if hours > h:
                left = mid + 1
            elif hours <= h:
                temp = mid
                right = mid - 1
        return temp