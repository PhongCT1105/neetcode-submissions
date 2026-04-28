class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        length = 0 
        import heapq

        for num in nums:
            if length < k:
                length += 1
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)        

        return heap[0]