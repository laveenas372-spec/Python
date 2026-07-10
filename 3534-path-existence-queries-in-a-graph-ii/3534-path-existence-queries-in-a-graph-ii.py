
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
       
        arr = sorted((v, i) for i, v in enumerate(nums))

        pos = [0] * n
        comp = [0] * n

        cid = 0
        pos[arr[0][1]] = 0

        for i in range(n):
            if i:
                if arr[i][0] - arr[i - 1][0] > maxDiff:
                    cid += 1
            comp[i] = cid
            pos[arr[i][1]] = i

        reach = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and arr[j + 1][0] - arr[i][0] <= maxDiff:
                j += 1
            reach[i] = j

        LOG = n.bit_length()
        up = [reach]

        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            a = pos[u]
            b = pos[v]

            if comp[a] != comp[b]:
                ans.append(-1)
                continue

            if a == b:
                ans.append(0)
                continue

            if a > b:
                a, b = b, a

            cur = a
            steps = 0

            for k in range(LOG - 1, -1, -1):
                nxt = up[k][cur]
                if nxt < b:
                    cur = nxt
                    steps += 1 << k

            ans.append(steps + 1)

        return ans