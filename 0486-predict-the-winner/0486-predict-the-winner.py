class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}
        def maxDiff(left,right):
            if left == right:
                return nums[left]
            if (left,right) in memo:
                return memo[(left,right)]

            pickLeft = nums[left] - maxDiff(left + 1, right)
            pickRight = nums[right] - maxDiff(left,right -1)

            memo[(left,right)]= max(pickLeft,pickRight)
            return memo[(left,right)]

        return maxDiff(0,len(nums)-1) >= 0        