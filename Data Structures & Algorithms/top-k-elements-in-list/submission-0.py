class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        hash_num = Counter(nums)
        cnt_num = [(v,k) for (k,v) in hash_num.items()]
        heap = []

        import heapq

        for num in cnt_num:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                min_heap = heap[0]
                if min_heap[0] < num[0]:
                    heapq.heappushpop(heap, num)
        
        res = [i[1] for i in heap]
        return res