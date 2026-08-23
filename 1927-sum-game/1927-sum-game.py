class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)

        def gets(s):
            nn = qq = 0
            for ch in s:
                if ch == "?":
                    qq += 1
                else:
                    nn += int(ch)
            return nn,qq
        
        n0,q0 = gets(num[: n//2])
        n1,q1 = gets(num[n//2 : ])

        return (q0 + q1) % 2 == 1 or n0 - n1 != (q1-q0)*9//2
        