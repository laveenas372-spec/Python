class Solution(object):
    def smallestNumber(self, n, t):
        while True:

            num = 1
            for i in str(n):
                num *= int(i)
            if num % t == 0:
                return n
            n += 1