class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Initialize L and R pointers
        int L = 0;
        int R = 0;
        int maxLength = 0;

        // Initialize a HashMap
        HashMap<Character, Boolean> hashMap = new HashMap<>();

        // Iterate over s using while loop:
        // L starts at 0 and R starts at 0
        // While HashMap contains R, make window smaller via L side until HashMap no longer contains R
        // Add s[R] to HashMap and increment R
        while (R < s.length()) {
            while (hashMap.containsKey(s.charAt(R))) {
                hashMap.remove(s.charAt(L));
                L++;
            }

            hashMap.put(s.charAt(R), true);
            maxLength = Math.max(maxLength, R - L + 1);
            R++;
        }
        
        return maxLength;
    }
}
