class Solution:
    def sumOfSquares(self, n: int) -> int:
        return sum(int(digit)**2 for digit in str(n))
            
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            if slow == 1:
                return True
            if slow == fast:
                return False
            

            
