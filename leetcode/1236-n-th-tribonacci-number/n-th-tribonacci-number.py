class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [-1] * (n+1)
    
        if n >= 0:
            ans[0] = 0
        if n >= 1:
            ans[1] = 1
        if n >= 2: 
            ans[2] = 1

        def fib(n):
            if ans[n] != -1:
                return ans[n]
            ans[n] = fib(n - 1) + fib(n - 2) + fib(n - 3)
            return ans[n]
        
        return fib(n)
        