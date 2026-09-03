class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        mn = nums1[0]
        hasOdd = False
        for v in nums1:
            if v < mn:
                mn = v
            if v & 1:
                hasOdd = True
        if mn & 1:
            return True
        return not hasOdd