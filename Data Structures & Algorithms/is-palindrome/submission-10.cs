public class Solution {
    public bool IsPalindrome(string s) {
        string cleaned = new string(s.Where(char.IsLetterOrDigit).ToArray());
        int l = 0;
        int r = cleaned.Length - 1;
        cleaned = cleaned.ToLowerInvariant();
        while (l < r) {
            if (cleaned[l] != cleaned[r]) {
                return false;
            }
            l += 1;
            r -= 1;
        }
        return true;
    }
}
