class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arrSorted = sorted(arr)

        mp = {}
        rank = 1
        
        for num in arrSorted:
            if num not in mp:
                mp[num] = rank
                rank += 1
        
        result = [mp[num] for num in arr]
        return result 