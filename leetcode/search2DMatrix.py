class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        first, last = 0, len(matrix) - 1
        while first <= last:
            row = first + (last - first) // 2

            if target < matrix[row][0]:
                last = row - 1
            elif target > matrix[row][-1]:
                first = row + 1
            else:
                break
        
        if first > last:
            return False
        
        correctRow = first + (last - first) // 2
        l, r = 0, len(matrix[correctRow]) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if target == matrix[correctRow][mid]:
                return True
            elif target < matrix[correctRow][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False