class Solution:
    def Pow(self, x, n):
        if n == 0:
            return 1
        a = self.Pow(x, n//2)
        if n%2 == 0:
            return a*a
        else:
            return a*a*x
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.Pow(x, n)
        return 1/self.Pow(x,n*(-1))