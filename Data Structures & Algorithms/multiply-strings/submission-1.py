class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # Calculate a digit to a full number
        # Num1: full number, Num2: single digit
        def calculate_multiply(num1: str, num2: str): 
            total = []
            for i in range(len(num1)-1, -1, -1):
                total.append(int(num1[i]) * int(num2))
                
            return total[::-1]

        total_multiply = []
        order = 1
        for num in num2:
            total_multiply.append(calculate_multiply(num1, num))

        res = 0
        for i in range(len(total_multiply)):
            total_sum = 0
            order = 1
            for j in range(len(total_multiply[i])-1, -1, -1):
                total_sum += total_multiply[i][j] * order
                order *= 10
            total_multiply[i] = total_sum
        
        res = 0
        order = 1
        for i in range(len(total_multiply)-1, -1, -1):
            res += total_multiply[i] * order
            order *= 10
        return str(res)