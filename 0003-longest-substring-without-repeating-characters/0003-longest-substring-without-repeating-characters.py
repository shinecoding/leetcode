class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        dup = set()

        for r in range(len(s)):
            # 이미 set에 있으면 중복 나온 지점까지 다 제거
            while s[r] in dup:
                dup.remove(s[l])
                l += 1
            dup.add(s[r])

            res = max(r -l +1, res)

        return res    