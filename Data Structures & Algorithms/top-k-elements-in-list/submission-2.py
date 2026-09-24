class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for num in nums:
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1

        import heapq
        heap = []
        # Min heap
        for num, freq in nums_map.items():
            if k > 0:
                heapq.heappush(heap, (freq,num))
                k -= 1
                continue
            if heap[0][0] < freq:
                heapq.heappushpop(heap, (freq,num))  
        
        return [num for frequency, num in heap]