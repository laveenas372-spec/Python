class Solution {
    typedef unsigned long long ull;
    const ull MOD = 1000000007ULL;

    bool check(vector<int>& nums, int len, ull base, int mn) {
        int n = nums.size();
        unordered_map<ull, int> freq;

        ull hash = 0, power = 1;
        for (int i = 0; i < len; i++) {
            hash = (hash * base + (nums[i] - mn + 1)) % MOD;
            if (i < len - 1) power = power * base % MOD;
        }
        freq[hash]++;

        for (int i = len; i < n; i++) {
            ull out = (nums[i - len] - mn + 1) * power % MOD;
            hash = (hash + MOD - out) % MOD;
            hash = (hash * base + (nums[i] - mn + 1)) % MOD;
            freq[hash]++;
        }

        for (auto& [h, c] : freq)
            if (c == 1) return true;
        return false;
    }

public:
    int smallestUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        int mn = *min_element(begin(nums), end(nums));
        ull base = *max_element(begin(nums), end(nums)) - mn + 2;

        int l = 1, r = n, result = n;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (check(nums, mid, base, mn)) { result = mid; r = mid - 1; }
            else l = mid + 1;
        }
        return result;
    }
};