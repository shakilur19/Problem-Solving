class Solution:
    def fib(self, n: int) -> int:
        ans = [-1] * (n+1)
        if n >= 0:
            ans[0] = 0
        if n >= 1:
            ans[1] = 1

        def re_fib(number):
            if ans[number] == -1:
                ans[number] = re_fib(number-1) + re_fib(number-2)
            return ans[number]
        
        return re_fib(n)

        