class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Initialize a HashMap
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] answer = new int[2];

        // Iterate through nums and for each element in nums check if it exists
        // within HashMap - if it does, we've found our answer and if it does not
        // we calculate its complement via target - nums[i] = complement. 
        // We then store complement in HashMap and map it to a value of i (e.g., complement : 0)
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                answer[0] = map.get(nums[i]);
                answer[1] = i; 
                break;
            }

            map.put(target - nums[i], i);
        }
        return answer;
    }
}
