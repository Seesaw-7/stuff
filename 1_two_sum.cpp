#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    static vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> sol;
        int i=0,j=0;
        for(int x:nums){
            j=0;
            for(int y:nums){
                if(x+y==target&&i!=j){
                    sol.push_back(i);
                    sol.push_back(j);
                    break;
                }
                j++;
            }
            i++;
        }
        return sol;
    }
};


int main(){

    vector<int> nums;
    vector<int> sol;
    int a,target;
    while(cin>>a){
        nums.push_back(a);
        char c=getchar();
        if(c=='\n'){
            break;
        }
    }
    nums.pop_back();
    target=a;
    sol=Solution::twoSum(nums,target);
    cout<<'['<<sol[0]<<','<<sol[1]<<']';
    
}