class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> unique = new HashSet<>();
        int numsLength = nums.length;
        for(int i = 0; i < numsLength; i++){
            if(unique.contains(nums[i])){
                return true;
            }
            unique.add(nums[i]);
        }

        return false;
    }
}
