class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        check = {}
        temp_1 = None
        for i in numbers:
            if (target - i) in check:
                result.append(check[(target - i)])
                result.append(numbers.index(i) + 1)
                return result
            else:
                check[i] = (numbers.index(i) + 1)
        return check




