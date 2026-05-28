class Solution:

    def isHappy(self, n: int) -> bool:
        visit = set()
        total = n
        def calculate(number: int) -> int:
            total = 0
            while number > 0:
                digit = number % 10
                total += digit ** 2
                number = number // 10
            return total

        while total != 1:
            total = calculate(total)
            if total == 1:
                return True
            if total in visit:
                return False
            visit.add(total)

