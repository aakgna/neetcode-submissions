class Solution {
    public int[] productExceptSelf(int[] nums) {
        int zero = 0;
        int product = 1;
        for (int num : nums) {
            if (num == 0) {
                zero += 1;
                continue;
            }
            product *= num;
        }
        int[] res = new int[nums.length];
        if (zero > 1) {
            return res;
        }
        else if (zero == 1) {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] == 0) {
                    res[i] = product;
                    continue;
                }
                res[i] = 0;
            }
        }
        else {
            for (int i = 0; i < nums.length; i++) {
                res[i] = product / nums[i];
            }
        }
        return res;
    }
}  
