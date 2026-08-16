class Solution:
    def stoneGameIX(self, stones):

        # Count stones based on their remainder when divided by 3
        count0 = 0
        count1 = 0
        count2 = 0

        for ele in stones:

            if ele % 3 == 0:
                count0 += 1
            elif ele % 3 == 1:
                count1 += 1
            else:
                count2 += 1

        # If count of remainder 0 stones is even
        if count0 % 2 == 0:
            return count1 >= 1 and count2 >= 1

        # If count of remainder 0 stones is odd
        return abs(count1 - count2) > 2