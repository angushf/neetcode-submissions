class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Initialize HashSet
        HashSet<Integer> set = new HashSet<>();

        // Iterate over nums array, check if nums[i] is in HashSet, if it is, it's a duplicate
        // and return true, if not then add nums[i] to HashSet
        for (int num : nums) {
            if (set.contains(num)) {
                return true;
            }

            set.add(num);
        }
        
        return false;
    }
}