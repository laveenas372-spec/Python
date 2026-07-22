import bisect


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.seg = [0] * (4 * max(1, self.n))

        if self.n:
            self.build(1, 0, self.n - 1)

    def build(self, p, l, r):
        if l == r:
            self.seg[p] = self.arr[l]
            return

        mid = (l + r) >> 1

        self.build(p << 1, l, mid)
        self.build((p << 1) | 1, mid + 1, r)

        self.seg[p] = max(
            self.seg[p << 1],
            self.seg[(p << 1) | 1]
        )

    def query(self, L, R):
        if self.n == 0 or L > R:
            return 0

        return self._query(1, 0, self.n - 1, L, R)

    def _query(self, p, l, r, L, R):
        if L <= l and r <= R:
            return self.seg[p]

        mid = (l + r) >> 1
        res = 0

        if L <= mid:
            res = max(
                res,
                self._query(p << 1, l, mid, L, R)
            )

        if R > mid:
            res = max(
                res,
                self._query((p << 1) | 1, mid + 1, r, L, R)
            )

        return res


class Solution(object):

    def maxActiveSectionsAfterTrade(self, s, queries):
        n, cnt1 = len(s), s.count('1')

        blockLeft, blockRight, zeroBlocks = [], [], []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                blockLeft.append(start)
                blockRight.append(i - 1)
                zeroBlocks.append(i - start)
            else:
                i += 1

        m = len(zeroBlocks)
        tmpSum = [zeroBlocks[k] + zeroBlocks[k + 1] for k in range(m - 1)] if m > 1 else []
        st = SegmentTree(tmpSum)

        ans = []
        for l, r in queries:
            idx1 = bisect.bisect_left(blockRight, l)
            idx2 = bisect.bisect_right(blockLeft, r) - 1

            if idx1 > idx2 or idx1 >= m or idx2 < 0:
                ans.append(cnt1)
                continue
            if idx1 == idx2:
                ans.append(cnt1)
                continue

            z_i = min(blockRight[idx1], r) - max(blockLeft[idx1], l) + 1
            z_j = min(blockRight[idx2], r) - max(blockLeft[idx2], l) + 1

            val1 = z_i + zeroBlocks[idx1 + 1] if idx1 + 1 <= idx2 else 0
            if idx1 + 1 == idx2:
                val1 = z_i + z_j

            val2 = zeroBlocks[idx2 - 1] + z_j if idx2 - 1 >= idx1 else 0
            if idx2 - 1 == idx1:
                val2 = z_i + z_j

            val3 = st.query(idx1 + 1, idx2 - 2) if idx1 + 1 <= idx2 - 2 else 0

            ans.append(cnt1 + max(val1, val2, val3))

        return ans
        