class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> match = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int val = target - nums[i];
            if (match.containsKey(val)) {
                return new int[]{match.get(val), i};
            }
            match.put(nums[i], i);
        }
        return new int[]{0,0};
    }
}
