class Solution { 
public: 
    int sumOfSquares(vector<int>& nums) { 
        int sum = 0; 
        int n = nums.size(); 
        
        for (int i = 0; i < n; i++) { 
            // 1. Fixed the assignment error (i=1) to an addition (i+1)
            // 2. Used the equality operator == for the comparison
            if (n % (i + 1) == 0) {
                sum += (nums[i] * nums[i]); 
            }
        } 
        
        // 3. Moved the return statement inside the function body
        return sum; 
    } 
};