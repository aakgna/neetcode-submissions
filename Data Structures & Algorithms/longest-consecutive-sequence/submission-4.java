class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int res = 0;
        Set<Integer> set = new HashSet<>();
        for (int n : nums) {
            set.add(n);
        }

        for (int n : nums) {
            if (!set.contains(n-1)) {
                int val = n-1;
                int cnt = 0;
                while (set.contains(val+1)) {
                    cnt += 1;
                    val += 1;
                }
                res = Math.max(res, cnt);
            }
        }
        return res;
    }
}
