class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        replace = -1
        # Go from the right to the left
        # Replace with the largest so far on the right
        for i in range(len(arr)-1, -1, -1):
            old_val = arr[i]
            arr[i] = replace
            replace = max(old_val, replace)

        return arr