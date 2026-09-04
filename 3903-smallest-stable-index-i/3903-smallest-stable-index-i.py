class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            maxValue = minValue = nums[i]
            for j in range(i):
                maxValue = max(maxValue,nums[j])
            for j in range(i+1,n):
                minValue = min(minValue,nums[j])
            if maxValue - minValue <= k:
                return i
        return -1