class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        import heapq
        heap = []
        length = 0
        for num in hash_map.keys():
            key, value = num, hash_map[num]
            if length < k:
                heapq.heappush(heap, (value, key))
                length += 1
            else:
                heapq.heappushpop(heap, (value, key))

        res = [key for val, key in heap]
        return res