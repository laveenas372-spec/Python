class Solution {
public:
    int climbStairs(int n, vector<int>& costs) {
        
    vector<int> dp(n + 1, 0);

        for (int i = n-1; i >= 0; i--) {
            
            int cost = INT_MAX;

            int j = i + 1; 
            if(j <= n)                           // jump of 1
                cost = dp[j] + costs[j - 1] + (j - i) * (j - i);

            j = i + 2;                                  // jump of 2
            if (j <= n)
                cost = min(cost, dp[j] + costs[j - 1] + (j - i) * (j - i));

            j = i + 3;                                  // jump of 3
            if (j <= n)
                cost = min(cost, dp[j] + costs[j - 1] + (j - i) * (j - i));

            dp[i] = cost;
        }

        return dp[0];
    }
};


