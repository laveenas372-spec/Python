class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: i for i,c in reversed(list(enumerate(s)))}
        last = {c: i for i, c in enumerate(s)}

        def get_valid_right(i):
            right = last[s[i]]
            j = i
            while j<= right:
                if first[s[j]] < i: return -1
                right = max(right,last[s[j]])
                j += 1
            return right

        intervals = []
        for i in range(len(s)):
            if i == first[s[i]]:
                valid_right = get_valid_right(i)
                if valid_right != -1:
                    intervals.append((valid_right,i))

        intervals.sort()
        ans, last_end = [],-1
        for end,start in intervals:
            if start > last_end:
                ans.append(s[start:end+1])
                last_end = end
        return ans
        