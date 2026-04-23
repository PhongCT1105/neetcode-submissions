class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        all_value = self.hash_map[key]
        l, r = 0, len(all_value)

        while l < r:
            mid = (l + r) // 2
            
            if all_value[mid][1] == timestamp:
                return all_value[mid][0]
            
            if all_value[mid][1] > timestamp:
                l = mid + 1
            else:
                r = mid - 1

        return all_value[l][0]
