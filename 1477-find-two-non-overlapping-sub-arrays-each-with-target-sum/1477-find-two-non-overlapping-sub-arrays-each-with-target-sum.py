class Solution:

    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        # min_len[i] stores the minimum length of a valid sub-array ending at or before index i
        min_len = [float("inf")] * n

        prefix_sum_map = {0: -1}
        current_sum = 0
        min_total_length = float("inf")
        best_single_len = float("inf")

        for i in range(n):
            current_sum += arr[i]

            # Check if there is a sub-array ending at index i with sum equal to target
            if (current_sum - target) in prefix_sum_map:
                start_idx = prefix_sum_map[current_sum - target]
                current_len = i - start_idx

                # If a valid sub-array exists before start_idx + 1, update the global minimum total length
                if start_idx >= 0 and min_len[start_idx] != float("inf"):
                    min_total_length = min(
                        min_total_length, current_len + min_len[start_idx]
                    )

                # Update the best single sub-array length seen so far
                best_single_len = min(best_single_len, current_len)

            # Record the minimum sub-array length seen up to index i
            min_len[i] = best_single_len
            prefix_sum_map[current_sum] = i

        return min_total_length if min_total_length != float("inf") else -1    