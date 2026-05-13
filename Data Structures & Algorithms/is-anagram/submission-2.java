class Solution {
    public boolean isAnagram(String s, String t) {
        // Return false immediately if length of s and t don't match
        if (s.length() != t.length()) {
            return false;
        }

        // Initialize a HashMap
        HashMap<Character, Integer> map = new HashMap<>();

        /*
            Iterate over s and for each letter store it as letter: count
            in HashMap. Then iterate over t and for each letter, decrement the count
            in HashMap. If count ends up negative, return False. Then return true if HashMap 
            contains values that are only 0 and false otherwise.
        */
        for (char letter : s.toCharArray()) {
            if (map.containsKey(letter)) {
                int count = map.get(letter);
                map.put(letter, count + 1);
            } else {
                map.put(letter, 1);
            }
        }

        for (char letter : t.toCharArray()) {
            if (map.containsKey(letter)) {
                int currCount = map.get(letter);
                if (currCount == 0) {
                    return false;
                } else {
                    map.put(letter, currCount - 1);
                }
            } else {
                return false;
            }
        }

        for (int count : map.values()) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }
}
