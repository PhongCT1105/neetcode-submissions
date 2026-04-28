class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Iterate through the string
            # For each element check if they in the hash map:
                # If they not:
                # Keep increase the count of non duplicate
                # and add the element to the hash map
                
                # If they in:
                # Keep popping up from the last pointer for 
                # tracking the start of the non duplicate
                # Use this as the key to pop from the set
                # Keep popping until not
                # => Update the cnt
        if not s:
            return 0

        res, cnt = 0, 0
        hash_set = set()
        left = 0
        for c in s:
            while c in hash_set:
                hash_set.remove(s[left])
                left += 1
                cnt -= 1
            hash_set.add(c)
            cnt += 1
            res = max(res, cnt)

        return max(res, cnt)