class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        # Precompute LCM and sign for every non-empty subset
        subsets = []  # list of (lcm_value, sign)
        for mask in range(1, 1 << n):
            l = 1
            bits = 0
            overflow = False
            for i in range(n):
                if mask & (1 << i):
                    l = lcm(l, coins[i])
                    bits += 1
                    if l > 2 * 10**11:  # cap to avoid huge overflow, safe bound
                        overflow = True
                        break
            sign = 1 if bits % 2 == 1 else -1
            if not overflow:
                subsets.append((l, sign))
        
        def count_le(x):
            total = 0
            for l, sign in subsets:
                total += sign * (x // l)
            return total
        
        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo