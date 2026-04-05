class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        for i in matrix:
            for j in i:
                temp.append(j)
        right_pointer = len(temp) - 1
        left_pointer = 0
        while left_pointer <= right_pointer:
            mid = left_pointer + ((right_pointer - left_pointer) // 2)
            if target < temp[mid]:
                right_pointer = mid - 1
            elif target == temp[mid]:
                return True
            else:
                left_pointer = mid + 1
        return False
        