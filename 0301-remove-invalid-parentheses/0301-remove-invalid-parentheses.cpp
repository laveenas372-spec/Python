#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        // Step 1: minimum number of '(' and ')' to remove
        int leftRem = 0, rightRem = 0;
        for (char ch : s) {
            if (ch == '(') {
                leftRem++;
            } else if (ch == ')') {
                if (leftRem > 0) leftRem--;
                else rightRem++;
            }
        }

        unordered_set<string> result;
        string path;
        dfs(s, 0, 0, leftRem, rightRem, path, result);
        return vector<string>(result.begin(), result.end());
    }

private:
    void dfs(const string& s, int i, int openCnt, int lRem, int rRem,
             string& path, unordered_set<string>& result) {
        int n = s.size();

        // Pruning: not enough characters left to satisfy removals
        if (lRem + rRem > n - i) return;

        if (i == n) {
            if (lRem == 0 && rRem == 0 && openCnt == 0) {
                result.insert(path);
            }
            return;
        }

        char ch = s[i];

        // Option 1: remove the current parenthesis
        if (ch == '(' && lRem > 0) {
            dfs(s, i + 1, openCnt, lRem - 1, rRem, path, result);
        } else if (ch == ')' && rRem > 0) {
            dfs(s, i + 1, openCnt, lRem, rRem - 1, path, result);
        }

        // Option 2: keep the current character
        path.push_back(ch);
        if (ch == '(') {
            dfs(s, i + 1, openCnt + 1, lRem, rRem, path, result);
        } else if (ch == ')') {
            if (openCnt > 0) {  // only keep ')' if it has a match
                dfs(s, i + 1, openCnt - 1, lRem, rRem, path, result);
            }
        } else {
            dfs(s, i + 1, openCnt, lRem, rRem, path, result);
        }
        path.pop_back();
    }
};