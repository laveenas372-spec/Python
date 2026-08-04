class Solution(object):
    def findMissingElements(self, nums):
        st = set(nums)
        mn = min(nums)
        mx = max(nums)
        return [x for x in range(mn + 1, mx) if x not in st]