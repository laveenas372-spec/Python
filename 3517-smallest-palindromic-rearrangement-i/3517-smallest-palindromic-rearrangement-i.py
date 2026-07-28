class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        mid = n//2

        s=list(s)

        first_half = sorted(s[:mid])

        for i in range(mid):
            s[i] = first_half[i]

        for i in range(mid):
            s[n - 1 -i] = s[i]

        return"".join(s)