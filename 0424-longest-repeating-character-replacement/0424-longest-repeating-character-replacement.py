class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        # sliding window
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # total string length - max number of same letter > k
            while (r-l+1) - max(count.values()) > k:
                # remove l count, move l pointer
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res