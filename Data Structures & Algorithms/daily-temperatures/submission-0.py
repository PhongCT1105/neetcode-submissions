class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Store a monotonic stack that is decreasing -> when having a day larger than that, pop it and return the difference j-i
        # Store a res that can be access to update the result
        len_temperatures = len(temperatures)
        res = [0] * len_temperatures
        stack = []

        for i in range(len_temperatures):
            curr_temp = (temperatures[i], i)
            if not stack:
                stack.append(curr_temp)
            else:
                if curr_temp[0] <= stack[-1][0]: # In decreasing order
                    stack.append(curr_temp)
                else: 
                    while stack and curr_temp[0] > stack[-1][0]:
                        last_temp = stack.pop()
                        diff = curr_temp[1] - last_temp[1]
                        res[last_temp[1]] = diff
                    stack.append(curr_temp)
        return res
