class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        elif x == 0:
            return True

        num = x
        result = 0
        
        while(num>0):
            LD = num % 10
            result = result*10 + LD
            num //= 10

        if result == x:
            return True
        else:
            return False
        