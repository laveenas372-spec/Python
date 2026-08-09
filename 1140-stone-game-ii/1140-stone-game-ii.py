class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        memo = [[0] * len(piles) for _ in range(len(piles))]

        suffix_sum = piles[:]
        for i in range(len(suffix_sum) -2, -1 ,-1):
            suffix_sum[i] += suffix_sum[i + 1]
    
        def max_stones(curr_index, max_till_now):
            if curr_index + 2 * max_till_now >= len(suffix_sum):
                return suffix_sum[curr_index]
            if memo[curr_index][max_till_now] > 0:
                return memo[curr_index][max_till_now]

            res = float('inf')
            for X in range(1, 2 * max_till_now + 1):
                res = min(res, max_stones(curr_index + X , max(max_till_now,X)))

            memo[curr_index][max_till_now] = suffix_sum[curr_index] - res
            return memo[curr_index][max_till_now]

        return max_stones(0,1)