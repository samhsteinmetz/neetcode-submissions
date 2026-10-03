class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // move forward with right pointer until greater than answer 
        
        int right = numbers.size()-1;
        int left = 0;

        int size = numbers.size();

        while(right>left){
            int numRight = numbers[right];
            int numLeft = numbers[left];
            int sum = (numLeft+numRight);
            if (sum == target){
                return {left+1,right+1};
            }
            if (sum > target){
                right--;
            }else{
                left++;
            }
        }


        
        return {1, 2};
    }
};
