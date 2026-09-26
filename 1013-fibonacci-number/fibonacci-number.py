class Solution:

    def calcu(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n == 3:
            return 2 
        
        return self.calcu(n-1) + self.calcu(n-2)


    def fib(self, n: int) -> int:
        return self.calcu(n)
        