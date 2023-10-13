class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0){
            return 0;
        }
        int inputIndex = 1;
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != nums[inputIndex-1]){
                nums[inputIndex] = nums[i];
                inputIndex++;
            }
        }
        return inputIndex; // Index of last write incremented by one gives number of elements
    }
}