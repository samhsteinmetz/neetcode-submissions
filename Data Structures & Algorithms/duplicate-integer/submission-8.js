class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        nums = nums.sort();

        console.log(nums);

        for(let i = 0; i < nums.length-1; i++){
            if(nums[i] === nums[i+1]){
                return true;
            }
        }

        return false;
        
    }
}
