class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 1) {
            return 0;
        }

        if (s.length() == 1) {
            return 1;
        }

        // Initialize L and R pointers
        int L = 0;
        int R = 1;

        // Initialize HashMap
        HashMap<Character, Integer> map = new HashMap<>();
        map.put(s.charAt(L), L);

        // Initialize maxLength variable
        int maxLength = 0;

        // While R < s.length(), keep advancing R pointer by one until s[R] == s[L]. 
        // When this happens, we've found our first duplicate, so at this point we 
        // update maxLength with Math.max(R-L, maxLength) and increment L by one.
        while (R < s.length()) {
            if (map.containsKey(s.charAt(R))) {
                maxLength = Math.max(R - L, maxLength);
                int oldL = map.get(s.charAt(R));
                map.remove(s.charAt(oldL));
                L = Math.max(L, oldL + 1);  // never move L backwards
            }

            map.put(s.charAt(R), R);
            R++;
        }

        return Math.max(maxLength, R - L);
    }
}
