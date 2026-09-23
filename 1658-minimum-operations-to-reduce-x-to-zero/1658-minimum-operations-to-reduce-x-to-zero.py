class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target <  0:
            return -1

        max_len = -1
        current_sum = 0
        l = 0

        for r in range(len(nums)):
            current_sum += nums[r]
            
            while current_sum > target and l <= r:
                current_sum -= nums[l]
                l += 1
            if current_sum == target:
                max_len = max(max_len , r - l + 1)

            

        return len(nums) - max_len if max_len != -1 else -1