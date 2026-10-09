class Solution:
    def minInsertions(self, s: str) -> int:
        d = 0     # number of ')' still needed
        res = 0   # insertions made

        for c in s:
            if c == '(':
                d += 2
                if d % 2 == 1:   # previous '(' had only one ')', so insert one
                    res += 1
                    d -= 1
            else:  # c == ')'
                d -= 1
                if d < 0:        # no open '(' to match, so insert a '('
                    res += 1
                    d = 1        # the new '(' still needs one more ')'

        return res + d           # remaining ')' needed at the end