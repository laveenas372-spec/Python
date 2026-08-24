class Solution(object):
    def stoneGameVIII(self, stones):
        n = len(stones)

        pre = []
        s = 0
        for x in stones:
            s += x
            pre.append(s)

        f = [0] * n
        f[n - 1] = pre[n - 1]

        for i in range(n - 2, 0, -1):
            f[i] = max(f[i + 1], pre[i] - f[i + 1])

        return f[1]