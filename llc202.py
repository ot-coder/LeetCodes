class Solution:
    def isHappy(self, n: int) -> bool:
        def find_next(num):
            total = 0
            while num > 0:
                digit = num %10
                total += digit ** 2
                num //= 10
            return total

        found = set()
        while n!= 1 and n not in found:
            found.add(n)
            n = find_next(n)

        return n == 1
        