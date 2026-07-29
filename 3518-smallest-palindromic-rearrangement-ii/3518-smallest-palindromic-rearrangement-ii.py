class Solution(object):
    def smallestPalindrome(self, s, k):
        def comb(n, m, k_limit):
            res = 1
            m = min(m, n - m)
            for i in range(1, m + 1):
                res = res * (n - i + 1) // i
                if res > k_limit:
                    return k_limit + 1
            return res

        partition = len(s) // 2
        bucket = [0] * 26

        for ch in s:
            bucket[ord(ch) - 97] += 1

        def permutations(rem):
            ways = 1
            for i in range(26):
                if bucket[i] == 0:
                    continue
                cnt = bucket[i] // 2
                if cnt:
                    ways *= comb(rem, cnt, k)
                    rem -= cnt
                if ways > k:
                    return k + 1
            return ways

        if permutations(partition) < k:
            return ""

        left_half = []

        for pos in range(partition):
            found = False
            for i in range(26):
                if bucket[i] < 2:
                    continue
                bucket[i] -= 2
                ways = permutations(partition - pos - 1)
                if ways >= k:
                    left_half.append(chr(i + 97))
                    found = True
                    break
                else:
                    k -= ways
                    bucket[i] += 2
            if not found:
                return ""

        mid = ""
        for i in range(26):
            if bucket[i] % 2:
                mid = chr(i + 97)
                break

        left_str = "".join(left_half)
        return left_str + mid + left_str[::-1]