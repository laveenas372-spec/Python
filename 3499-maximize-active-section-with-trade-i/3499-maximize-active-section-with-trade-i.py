class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        t = "1" + s + "1"
        blocks=[]

        count = 0
        i = 0
        j = 0

        while j < len(t):
            if t[i] == t[j]:
                count += 1
                j += 1
                continue
            blocks.append(count)
            count = 0
            i = j
        blocks.append(count)

        max_gain = 0

        for i in range(2,len(blocks) -1,2):
            max_gain = max(max_gain, blocks[i - 1] + blocks[i + 1])

        one_count = 0

        for ch in s:
            if ch == '1':
                one_count += 1

        return one_count + max_gain