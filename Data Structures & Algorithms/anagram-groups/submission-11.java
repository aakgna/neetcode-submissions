class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> buckets = new HashMap<>();
        int base = 'a';
        for (int i = 0; i < strs.length; i++) {
            int[] counts = new int[26];
            for (int j = 0; j < strs[i].length(); j++) {
                counts[(int) strs[i].charAt(j) - base] += 1;
            }
            String enter = Arrays.toString(counts);
            buckets.putIfAbsent(enter, new ArrayList<>());
            buckets.get(enter).add(strs[i]);
        }
        return new ArrayList<>(buckets.values());
    }
}
