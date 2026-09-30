#include <vector>
#include <string>

using namespace std;


class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
    int n = seq.length();
    vector<int> result(n);
    int d=0 ;
    
    for (int i = 0; i < n; i++) {
        if (seq[i] == '('){
            d++;
            result[i] = (d%2);
            }
        else{
            result[i] = (d%2);
            d--;
            }
        }
    return result;
    }
};