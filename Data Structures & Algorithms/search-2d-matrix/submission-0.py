class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find which rows it's belong first
        n = len(matrix)
        l,r = 0,n-1
        found = False
        while l <= r:
            mid = (l+r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                found = True
                row = mid
                break
            elif target < matrix[mid][0]:
                r = mid-1
            else:
                l = mid+1
        if not found:
            return False
        # Find the exact place:
        l, r = 0, len(matrix[row])-1
        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid+1
            else:
                r = mid-1
        
        return False
            