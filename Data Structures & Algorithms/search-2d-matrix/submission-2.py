class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        left_pointer = 0
        right_pointer = (cols * rows) - 1
        while left_pointer <= right_pointer:
            mid = left_pointer + ((right_pointer - left_pointer) // 2)
            if matrix[mid // cols][mid % cols] > target:
                right_pointer = mid - 1
            elif matrix[mid // cols][mid % cols] == target:
                return True
            else:
                left_pointer = mid + 1
        return False